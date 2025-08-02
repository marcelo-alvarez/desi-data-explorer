#!/usr/bin/env python3
import numpy as np

def calculate_optimal_projection(ra, dec, z):
    """Test the wedge projection function"""
    
    # Convert to radians
    ra_rad = np.radians(ra)
    dec_rad = np.radians(dec)
    
    # Use RA directly as angle
    angle = ra_rad
    
    # Convert to Cartesian coordinates with redshift as radius
    x_proj = z * np.cos(angle)
    y_proj = z * np.sin(angle)
    
    return x_proj, y_proj, z

# Test with simple data: 4 galaxies at same redshift but different RA
ra = np.array([0, 90, 180, 270])   # 0°, 90°, 180°, 270° RA  
dec = np.array([0, 0, 0, 0])       # Same declination
z = np.array([1.0, 1.0, 1.0, 1.0]) # Same redshift

x, y, z_out = calculate_optimal_projection(ra, dec, z)
print('Input RA:', ra)
print('Input z:', z)
print('Output x:', x)
print('Output y:', y)
print('Distance from origin:', np.sqrt(x**2 + y**2))
print('Should all be 1.0 for circular contours!')

# Test different redshifts at same RA
ra2 = np.array([0, 0, 0])     # Same RA
dec2 = np.array([0, 0, 0])    # Same declination  
z2 = np.array([0.5, 1.0, 1.5]) # Different redshifts

x2, y2, z2_out = calculate_optimal_projection(ra2, dec2, z2)
print('\nDifferent redshifts at same angle:')
print('Input z:', z2)
print('Output x:', x2)
print('Output y:', y2)
print('Distance from origin:', np.sqrt(x2**2 + y2**2))
print('Should equal redshift values!')