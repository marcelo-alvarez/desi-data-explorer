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
from desi_data_access import DESIDataAccess

# Suppress routine warnings for cleaner output
warnings.filterwarnings('ignore', category=UserWarning)

def calculate_optimal_projection(ra, dec, z):
    """
    Calculate optimal projection plane to minimize angular spread.
    
    Parameters:
    -----------
    ra, dec, z : array-like
        Right ascension (degrees), declination (degrees), and redshift
        
    Returns:
    --------
    tuple
        (x_proj, y_proj, radius) for orthographic projection
    """
    
    # Convert to radians
    ra_rad = np.radians(ra)
    dec_rad = np.radians(dec)
    
    # Convert to Cartesian coordinates
    x = np.cos(dec_rad) * np.cos(ra_rad)
    y = np.cos(dec_rad) * np.sin(ra_rad)
    z_cart = np.sin(dec_rad)
    
    # Find mean direction (center of distribution)
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    mean_z = np.mean(z_cart)
    
    # Normalize to get projection center
    norm = np.sqrt(mean_x**2 + mean_y**2 + mean_z**2)
    center_x, center_y, center_z = mean_x/norm, mean_y/norm, mean_z/norm
    
    # Create orthonormal basis for projection plane
    # Use north celestial pole as reference for second vector
    north_x, north_y, north_z = 0, 0, 1
    
    # First tangent vector (cross product with north pole)
    t1_x = center_y * north_z - center_z * north_y
    t1_y = center_z * north_x - center_x * north_z
    t1_z = center_x * north_y - center_y * north_x
    
    # Normalize
    t1_norm = np.sqrt(t1_x**2 + t1_y**2 + t1_z**2)
    if t1_norm > 0:
        t1_x, t1_y, t1_z = t1_x/t1_norm, t1_y/t1_norm, t1_z/t1_norm
    else:
        # Fallback if parallel to north pole
        t1_x, t1_y, t1_z = 1, 0, 0
    
    # Second tangent vector (cross product)
    t2_x = center_y * t1_z - center_z * t1_y
    t2_y = center_z * t1_x - center_x * t1_z
    t2_z = center_x * t1_y - center_y * t1_x
    
    # Project points onto tangent plane (angular coordinates scaled by redshift)
    x_proj = (x * t1_x + y * t1_y + z_cart * t1_z) * z
    y_proj = (x * t2_x + y * t2_y + z_cart * t2_z) * z
    
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
    
    # Set equal aspect ratio for proper wedge shape
    ax.set_aspect('equal')
    
    # Styling
    ax.set_xlabel('Projected X Coordinate [redshift × angular]', fontsize=14)
    ax.set_ylabel('Projected Y Coordinate [redshift × angular]', fontsize=14)
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
        
        # Query galaxies
        print("Querying main survey galaxies...")
        galaxies = desi.query_galaxies(
            max_galaxies=50000,
            z_range=(0.0, 1.5),
            show_progress=True
        )
        
        if len(galaxies) == 0:
            print("ERROR: No galaxies retrieved from query!")
            return False
        
        # Create visualization
        output_path = "../figures/galaxy_wedge.png"
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