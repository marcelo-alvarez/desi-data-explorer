#!/usr/bin/env python3
"""
Galaxy Wedge Visualization for DESI DR1

This script creates a 2D wedge visualization of ~50,000 main survey galaxies
from DESI Data Release 1, showing their spatial distribution in an orthographic
projection with redshift-based coloring.

Usage:
    python galaxy_wedge_plot.py

Output:
    ../figures/galaxy_wedge.png
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import warnings
from src.desi_data_access import DESIDataAccess

# Suppress routine warnings for cleaner output
warnings.filterwarnings('ignore', category=UserWarning)

def calculate_optimal_projection(ra, dec, z):
    """
    Calculate proper wedge projection where constant redshift forms circles.
    
    CRITICAL REQUIREMENT: In a wedge plot, galaxies at the SAME redshift 
    MUST form circular contours centered at the origin.
    
    This requires: x² + y² = (redshift)² for constant-redshift galaxies
    
    Parameters:
    -----------
    ra, dec, z : array-like
        Right ascension (degrees), declination (degrees), and redshift
        
    Returns:
    --------
    tuple
        (x_proj, y_proj, radius) for wedge projection
    """
    
    # Convert to radians
    ra_rad = np.radians(ra)
    dec_rad = np.radians(dec)
    
    # CORRECT WEDGE MATHEMATICS:
    # For each galaxy: (x, y) = redshift * (cos(angle), sin(angle))
    # where angle is derived from sky position (RA, Dec)
    
    # Convert (RA, Dec) to a single angular coordinate
    # We need to map 2D sky position to 1D angle for polar coordinates
    
    # Method: Use RA directly as angle, but weight by Dec to avoid pole issues
    # This creates a natural mapping from sky to polar coordinates
    
    # Option 1: Simple RA mapping (may have issues at poles)
    angle = ra_rad
    
    # Convert to Cartesian coordinates with redshift as radius
    x_proj = z * np.cos(angle)
    y_proj = z * np.sin(angle)
    
    # VERIFICATION: For constant z, x² + y² = z² * (cos²θ + sin²θ) = z²
    # This guarantees constant redshift forms perfect circles!
    
    return x_proj, y_proj, z

def create_wedge_plot(galaxies, output_path):
    """
    Create the galaxy wedge visualization.
    
    Parameters:
    -----------
    galaxies : pd.DataFrame
        Galaxy data with RA, DEC, Z columns
    output_path : str
        Path to save the figure
    """
    
    print(f"Creating wedge plot for {len(galaxies)} galaxies...")
    
    # Calculate projection coordinates
    x_proj, y_proj, redshift = calculate_optimal_projection(
        galaxies['RA'].values, 
        galaxies['DEC'].values, 
        galaxies['Z'].values
    )
    
    # Create the plot
    plt.style.use('default')
    fig, ax = plt.subplots(1, 1, figsize=(12, 10), dpi=100)
    
    # Create custom colormap for redshift
    colors = ['#000080', '#0000FF', '#00FFFF', '#00FF00', '#FFFF00', '#FF8000', '#FF0000']
    n_bins = 256
    cmap = LinearSegmentedColormap.from_list('redshift', colors, N=n_bins)
    
    # Create scatter plot
    scatter = ax.scatter(x_proj, y_proj, c=redshift, cmap=cmap, 
                        s=0.5, alpha=0.7, rasterized=True)
    
    # Set equal axis ranges with 1:1 aspect ratio
    x_range = np.max(np.abs(x_proj))
    y_range = np.max(np.abs(y_proj)) 
    max_range = max(x_range, y_range)
    ax.set_xlim(-max_range, max_range)
    ax.set_ylim(-max_range, max_range)
    ax.set_aspect('equal')
    
    # Styling
    ax.set_xlabel('Wedge X Coordinate [redshift × ΔRA]', fontsize=14)
    ax.set_ylabel('Wedge Y Coordinate [redshift × ΔDec]', fontsize=14)
    ax.set_title('DESI DR1 Galaxy Distribution: 2D Wedge Projection\n' + 
                f'{len(galaxies):,} Main Survey Galaxies', fontsize=16, pad=20)
    
    # Add colorbar
    cbar = plt.colorbar(scatter, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label('Redshift (z)', fontsize=14)
    cbar.ax.tick_params(labelsize=12)
    
    # Grid and styling
    ax.grid(True, alpha=0.3)
    ax.tick_params(labelsize=12)
    
    # Add statistics text box
    z_mean = np.mean(redshift)
    z_std = np.std(redshift)
    z_min, z_max = np.min(redshift), np.max(redshift)
    
    stats_text = f'Redshift Statistics:\n' \
                f'Mean: {z_mean:.3f} ± {z_std:.3f}\n' \
                f'Range: {z_min:.3f} - {z_max:.3f}\n' \
                f'Survey: DESI Main'
    
    ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, fontsize=11,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    # Tight layout
    plt.tight_layout()
    
    # Save the figure
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"Wedge plot saved to: {output_path}")
    
    # Show some statistics
    print(f"\nGalaxy Sample Statistics:")
    print(f"  Total galaxies: {len(galaxies):,}")
    print(f"  Redshift range: {z_min:.3f} - {z_max:.3f}")
    print(f"  Mean redshift: {z_mean:.3f} ± {z_std:.3f}")
    print(f"  RA range: {galaxies['RA'].min():.1f}° - {galaxies['RA'].max():.1f}°")
    print(f"  Dec range: {galaxies['DEC'].min():.1f}° - {galaxies['DEC'].max():.1f}°")
    
    return fig, ax

def main():
    """Main execution function."""
    
    print("DESI DR1 Galaxy Wedge Visualization")
    print("=" * 40)
    
    try:
        # Initialize data access
        print("Initializing DESI data access...")
        desi = DESIDataAccess()
        
        # Query all galaxy tracer types (LRGs, ELGs, QSOs)
        print("Querying all galaxy tracer types (LRGs, ELGs, QSOs)...")
        galaxies = desi.query_all_tracers(
            max_galaxies=50000,
            show_progress=True
        )
        
        if len(galaxies) == 0:
            print("ERROR: No galaxies retrieved from query!")
            return False
        
        # Create visualization
        output_path = "figures/galaxy_wedge.png"
        fig, ax = create_wedge_plot(galaxies, output_path)
        
        print("\n" + "=" * 40)
        print("Galaxy wedge visualization completed successfully!")
        print(f"Output saved to: {output_path}")
        print("\nPlease review the figure and provide approval before proceeding.")
        
        return True
        
    except Exception as e:
        print(f"ERROR: Visualization failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)