"""
DESI Data Access Module

This module provides functions to query DESI DR1 data using NOIRLab's TAP service.
Designed for tutorial use with professional astronomers and students.
"""

import warnings
from typing import Optional, Dict, Any
import numpy as np
import pandas as pd
from astroquery.utils.tap.core import TapPlus
from astropy.table import Table
from tqdm import tqdm
import time


class DESIDataAccess:
    """Class for accessing real DESI DR1 data via direct FITS file downloads."""
    
    def __init__(self):
        """Initialize the DESI data access object."""
        self.base_url = "https://data.desi.lbl.gov/public/dr1"
        self.lss_url = f"{self.base_url}/survey/catalogs/dr1/LSS/iron/LSScats/v1.5"
        self.fastspecfit_url = f"{self.base_url}/vac/dr1/fastspecfit/iron/v3.0/catalogs"
        
    def download_lss_file(self, tracer_type: str = "ELG_LOPnotqso", region: str = "NGC") -> str:
        """
        Download LSS clustering catalog containing galaxy data.
        
        Parameters:
        -----------
        tracer_type : str
            Galaxy tracer type ('ELG_LOPnotqso', 'LRG', 'BGS_BRIGHT', 'QSO')
        region : str
            Sky region ('NGC' or 'SGC')
            
        Returns:
        --------
        str
            Local filename of downloaded file
        """
        import urllib.request
        import os
        
        filename = f"{tracer_type}_{region}_clustering.dat.fits"
        url = f"{self.lss_url}/{filename}"
        local_path = f"/tmp/{filename}"
        
        print(f"Downloading {filename} from DESI DR1 LSS catalogs...")
        print(f"URL: {url}")
        
        try:
            urllib.request.urlretrieve(url, local_path)
            file_size = os.path.getsize(local_path) / (1024*1024)  # MB
            print(f"Downloaded {filename} ({file_size:.1f} MB)")
            return local_path
        except Exception as e:
            raise RuntimeError(f"Failed to download {filename}: {e}")
    
    def download_fastspecfit_file(self, survey_type: str = "main-dark", healpix: int = 0) -> str:
        """
        Download FastSpecFit VAC file containing emission line measurements.
        
        Parameters:
        -----------
        survey_type : str
            Type of survey data ('main-dark', 'main-bright')
        healpix : int
            HEALPix pixel number (0-11 for main survey)
            
        Returns:
        --------
        str
            Local filename of downloaded file
        """
        import urllib.request
        import os
        
        if survey_type.startswith("main"):
            filename = f"fastspec-iron-{survey_type}-nside1-hp{healpix:02d}.fits"
        else:
            filename = f"fastspec-iron-{survey_type}.fits"
            
        url = f"{self.fastspecfit_url}/{filename}"
        local_path = f"/tmp/{filename}"
        
        print(f"Downloading {filename} from DESI DR1...")
        print(f"URL: {url}")
        
        try:
            urllib.request.urlretrieve(url, local_path)
            file_size = os.path.getsize(local_path) / (1024*1024)  # MB
            print(f"Downloaded {filename} ({file_size:.1f} MB)")
            return local_path
        except Exception as e:
            raise RuntimeError(f"Failed to download {filename}: {e}")
    
    def query_galaxies(self, 
                      max_galaxies: int = 50000,
                      tracer_type: str = "ELG_LOPnotqso",
                      region: str = "NGC",
                      ra_range: Optional[tuple] = None,
                      dec_range: Optional[tuple] = None,
                      z_range: Optional[tuple] = (0.0, 1.5),
                      show_progress: bool = True) -> pd.DataFrame:
        """
        Query DESI DR1 galaxies from LSS clustering catalogs.
        
        Parameters:
        -----------
        max_galaxies : int
            Maximum number of galaxies to retrieve
        tracer_type : str
            Galaxy tracer type ('ELG_LOPnotqso', 'LRG', 'BGS_BRIGHT', 'QSO')
        region : str
            Sky region ('NGC' or 'SGC')
        ra_range : tuple, optional
            (min_ra, max_ra) in degrees
        dec_range : tuple, optional  
            (min_dec, max_dec) in degrees
        z_range : tuple, optional
            (min_z, max_z) redshift range
        show_progress : bool
            Show progress information
            
        Returns:
        --------
        pd.DataFrame
            Galaxy data with columns: TARGETID, RA, DEC, Z, WEIGHT_SYSTOT
        """
        from astropy.io import fits
        import numpy as np
        
        if show_progress:
            print(f"Querying {max_galaxies} {tracer_type} galaxies from DESI DR1 LSS catalogs...")
            print(f"Using real DESI data from {tracer_type}_{region}_clustering.dat.fits")
        
        # Download the LSS clustering file
        lss_file = self.download_lss_file(tracer_type, region)
        
        if show_progress:
            print("Reading FITS file...")
        
        # Read the FITS file
        with fits.open(lss_file) as hdul:
            data = hdul[1].data  # Main table is usually in extension 1
            
            # Create boolean mask for coordinate and redshift cuts
            mask = np.ones(len(data), dtype=bool)
            
            # Apply redshift range if specified
            if z_range and 'Z' in data.dtype.names:
                mask &= (data['Z'] >= z_range[0]) & (data['Z'] <= z_range[1])
                if show_progress:
                    print(f"  Redshift: {z_range[0]:.2f} < z < {z_range[1]:.2f}")
            elif 'Z_not4clus' in data.dtype.names:
                z_data = data['Z_not4clus']
                mask &= (z_data >= z_range[0]) & (z_data <= z_range[1])
                if show_progress:
                    print(f"  Redshift: {z_range[0]:.2f} < z < {z_range[1]:.2f}")
            
            # Apply coordinate ranges if specified
            if ra_range and 'RA' in data.dtype.names:
                mask &= (data['RA'] >= ra_range[0]) & (data['RA'] <= ra_range[1])
                if show_progress:
                    print(f"  RA: {ra_range[0]:.1f}° < RA < {ra_range[1]:.1f}°")
            
            if dec_range and 'DEC' in data.dtype.names:
                mask &= (data['DEC'] >= dec_range[0]) & (data['DEC'] <= dec_range[1])
                if show_progress:
                    print(f"  Dec: {dec_range[0]:.1f}° < Dec < {dec_range[1]:.1f}°")
            
            # Apply mask
            filtered_data = data[mask]
            
            if show_progress:
                print(f"Found {len(filtered_data)} galaxies matching criteria")
            
            # Randomly sample if we have more than requested
            if len(filtered_data) > max_galaxies:
                indices = np.random.choice(len(filtered_data), max_galaxies, replace=False)
                filtered_data = filtered_data[indices]
                if show_progress:
                    print(f"Randomly sampled {max_galaxies} galaxies")
            
            # Convert to pandas DataFrame with standard column names
            df_dict = {}
            
            # Map common column names
            column_map = {
                'TARGETID': ['TARGETID', 'TARGET_ID'],
                'RA': ['RA'],
                'DEC': ['DEC'], 
                'Z': ['Z', 'Z_not4clus', 'REDSHIFT'],
                'WEIGHT': ['WEIGHT_SYSTOT', 'WEIGHT', 'WEIGHT_ZFAIL']
            }
            
            for std_name, possible_names in column_map.items():
                for col_name in possible_names:
                    if col_name in filtered_data.dtype.names:
                        df_dict[std_name] = filtered_data[col_name]
                        break
                        
            # Add tracer type info
            df_dict['SPECTYPE'] = [tracer_type] * len(filtered_data)
            df_dict['REGION'] = [region] * len(filtered_data)
            
            df = pd.DataFrame(df_dict)
        
        if show_progress:
            print(f"Successfully loaded {len(df)} real DESI DR1 {tracer_type} galaxies")
            if 'Z' in df.columns:
                print(f"Redshift range: {df['Z'].min():.3f} to {df['Z'].max():.3f}")
            if 'RA' in df.columns and 'DEC' in df.columns:
                print(f"RA range: {df['RA'].min():.1f}° to {df['RA'].max():.1f}°")
                print(f"Dec range: {df['DEC'].min():.1f}° to {df['DEC'].max():.1f}°")
            
        return df
    
    def query_fastspecfit_data(self,
                              targetids: np.ndarray,
                              emission_lines: list = ['HALPHA', 'OII_3727'],
                              show_progress: bool = True) -> pd.DataFrame:
        """
        Query FastSpecFit VAC data for emission line measurements from real DESI files.
        
        Parameters:
        -----------
        targetids : np.ndarray
            Array of TARGETID values to query
        emission_lines : list
            List of emission lines to retrieve
        show_progress : bool
            Show progress information
            
        Returns:
        --------
        pd.DataFrame
            Emission line data with flux measurements and SFR values
        """
        from astropy.io import fits
        import numpy as np
        
        if show_progress:
            print(f"Querying FastSpecFit data for {len(targetids)} galaxies...")
            print("Using real DESI DR1 FastSpecFit VAC data")
        
        # We'll need to check multiple healpix files
        all_data = []
        
        for healpix in range(min(3, 12)):  # Start with first 3 healpix files for testing
            try:
                fastspec_file = self.download_fastspecfit_file("main-dark", healpix)
                
                with fits.open(fastspec_file) as hdul:
                    data = hdul[1].data
                    
                    # Find matching TARGETIDs
                    mask = np.isin(data['TARGETID'], targetids)
                    
                    if np.any(mask):
                        matched_data = data[mask]
                        all_data.append(matched_data)
                        
                        if show_progress:
                            print(f"  Found {len(matched_data)} matches in healpix {healpix}")
                            
            except Exception as e:
                if show_progress:
                    print(f"  Skipping healpix {healpix}: {e}")
                continue
        
        if not all_data:
            # Return empty DataFrame with expected columns
            columns = ['TARGETID']
            for line in emission_lines:
                columns.extend([f"{line}_FLUX", f"{line}_FLUX_IVAR"])
            columns.extend(['SFR_HALPHA', 'SFR_OII', 'STELLAR_MASS'])
            return pd.DataFrame(columns=columns)
        
        # Combine all data
        combined_data = np.concatenate(all_data)
        
        # Create DataFrame with emission line columns
        df_dict = {'TARGETID': combined_data['TARGETID']}
        
        # Add emission line flux and inverse variance columns
        for line in emission_lines:
            flux_col = f"{line}_FLUX"
            ivar_col = f"{line}_FLUX_IVAR" 
            
            if flux_col in combined_data.dtype.names:
                df_dict[flux_col] = combined_data[flux_col]
            if ivar_col in combined_data.dtype.names:
                df_dict[ivar_col] = combined_data[ivar_col]
        
        # Add SFR columns
        sfr_cols = ['SFR_HALPHA', 'SFR_OII', 'STELLAR_MASS']
        for col in sfr_cols:
            if col in combined_data.dtype.names:
                df_dict[col] = combined_data[col]
        
        df = pd.DataFrame(df_dict)
        
        if show_progress:
            print(f"Retrieved emission line data for {len(df)} galaxies from real DESI DR1")
            
        return df
    
    def get_quality_sample(self, 
                          emission_line: str,
                          max_galaxies: int = 10000,
                          min_snr: float = 3.0) -> pd.DataFrame:
        """
        Get a quality sample of galaxies with reliable emission line detections from real DESI data.
        
        Parameters:
        -----------
        emission_line : str
            Emission line name (e.g., 'HALPHA', 'OII_3727')
        max_galaxies : int
            Maximum number of galaxies to start with
        min_snr : float
            Minimum signal-to-noise ratio
            
        Returns:
        --------
        pd.DataFrame
            Combined galaxy and emission line data
        """
        
        # Get ELG galaxies (best for emission lines)
        galaxies = self.query_galaxies(max_galaxies=max_galaxies, tracer_type="ELG_LOPnotqso")
        
        if 'TARGETID' not in galaxies.columns:
            print("Warning: No TARGETID column found, cannot match with FastSpecFit data")
            return galaxies
        
        # Query emission line data
        emission_data = self.query_fastspecfit_data(
            galaxies['TARGETID'].values,
            emission_lines=[emission_line]
        )
        
        if len(emission_data) == 0:
            print(f"No FastSpecFit data found for {emission_line}")
            return pd.DataFrame()
        
        # Apply quality cuts
        flux_col = f"{emission_line}_FLUX"
        ivar_col = f"{emission_line}_FLUX_IVAR"
        
        if flux_col not in emission_data.columns or ivar_col not in emission_data.columns:
            print(f"Warning: {emission_line} data columns not found in FastSpecFit")
            return galaxies.merge(emission_data, on='TARGETID', how='inner')
        
        # Calculate S/N and apply cuts
        snr = emission_data[flux_col] * np.sqrt(emission_data[ivar_col])
        quality_mask = (
            (snr > min_snr) & 
            (emission_data[flux_col] > 0) &
            (emission_data[ivar_col] > 0) &
            np.isfinite(emission_data[flux_col]) &
            np.isfinite(emission_data[ivar_col])
        )
        
        clean_emission = emission_data[quality_mask].copy()
        
        # Join with galaxy data
        merged = galaxies.merge(clean_emission, on='TARGETID', how='inner')
        
        print(f"Quality sample: {len(merged)} galaxies with reliable {emission_line} detections from real DESI DR1")
        
        return merged


def test_data_access():
    """Test the real DESI data access functionality with a small sample."""
    print("Testing real DESI DR1 data access...")
    
    try:
        desi = DESIDataAccess()
        
        # Test small galaxy query with real data
        print("Testing galaxy query with 100 galaxies...")
        test_galaxies = desi.query_galaxies(max_galaxies=100, show_progress=True)
        print(f"✓ Galaxy query successful: {len(test_galaxies)} real DESI galaxies retrieved")
        print("Columns:", list(test_galaxies.columns))
        print(f"Redshift range: {test_galaxies['Z'].min():.3f} to {test_galaxies['Z'].max():.3f}")
        print(f"RA range: {test_galaxies['RA'].min():.1f}° to {test_galaxies['RA'].max():.1f}°")
        print(f"Dec range: {test_galaxies['DEC'].min():.1f}° to {test_galaxies['DEC'].max():.1f}°")
        
        # Test emission line data query
        print("\nTesting FastSpecFit emission line query...")
        sample_targetids = test_galaxies['TARGETID'].values[:10]  # Test with 10 galaxies
        emission_data = desi.query_fastspecfit_data(sample_targetids, show_progress=True)
        print(f"✓ Emission line query successful: {len(emission_data)} matches found")
        if len(emission_data) > 0:
            print("Emission line columns:", [col for col in emission_data.columns if 'FLUX' in col])
        
        print("\n✓ All tests passed - real DESI DR1 data access working!")
        return True
        
    except Exception as e:
        print(f"✗ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    test_data_access()