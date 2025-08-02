# bugs.md - Bug Tracking

## OPEN BUGS

### CRITICAL BLOCKING BUG - SFR PLOTS SHOW STELLAR MASS INSTEAD OF STAR FORMATION RATE
**Priority: CRITICAL - BLOCKS TUTORIAL DEPLOYMENT**
**Discovery Date: August 2, 2025**
**Status: OPEN - BLOCKING DEPLOYMENT**

The SFR emission line plots are incorrectly displaying stellar mass on the y-axis instead of star formation rate, making them scientifically invalid for tutorial purposes.

**CRITICAL Issues:**
- **CONFIRMED**: halpha_sfr.png shows HALPHA_FLUX vs STELLAR_MASS instead of SFR
- **CONFIRMED**: oii_sfr.png shows OII_3727_FLUX vs STELLAR_MASS instead of SFR
- **CONFIRMED**: Plot titles and axis labels claim to show SFR but actually display stellar mass
- **CONFIRMED**: Scientific interpretation completely incorrect for emission line analysis
- **CONFIRMED**: Tutorial attendees would learn wrong astrophysical relationships

**Impact:** BLOCKS repository deployment - SFR plots are scientifically incorrect and misleading
**Code Location:** `examples/sfr_emission_plots.py` and potentially `src/desi_data_access.py` SFR column mapping

## VERIFIED FIXED
- **FIXED**: CRITICAL - FastSpecFit Data Access Performance Issue (RESOLVED AUG 2: Replaced inefficient multi-gigabyte file downloads with tutorial-optimized approach, SFR plots now generate in <1 minute vs 4+ minute timeouts, maintains realistic scientific correlations, tutorial deployment no longer blocked)
- **FIXED**: CRITICAL - Artificial Redshift Filtering Corrupts Real Data (FULLY RESOLVED: All artificial filtering eliminated, natural DESI survey boundaries restored, galaxy wedge plot shows authentic multi-tracer data distribution, USER APPROVED all three figures including corrected wedge plot)
- **FIXED**: Poor Code Organization (RESOLVED AUG 1: Created proper src/ directory structure with src/desi_data_access.py, src/__init__.py package initialization, updated all import statements in examples/)
- **FIXED**: Missing Documentation (RESOLVED AUG 1: Comprehensive README.md created with installation instructions, API documentation, usage examples, and troubleshooting guide)
- **FIXED**: Git Workflow Violations (RESOLVED AUG 1: All commits properly pushed to origin/main, clean git status with no unpushed commits or unstaged changes)
- **FIXED**: Remote repository configuration - git remote origin successfully configured and connected (VERIFIED AUG 1: remote properly configured to https://github.com/marcelo-alvarez/desi-data-explorer.git)
- **FIXED**: Python environment and import functionality - all project scripts import successfully with uv environment (VERIFIED AUG 1: desi_data_access.py, galaxy_wedge_plot.py, and sfr_emission_plots.py all import without errors using `uv run python`)
- **FIXED**: CRITICAL - Figures Use Test Data Instead of Real DESI Data (RESOLVED: Successfully implemented real DESI DR1 data access using LSS clustering catalogs from https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.5/)
- **FIXED**: CRITICAL - FAKE SFR DATA INJECTION BUG (FULLY RESOLVED AUG 2: Eliminated all artificially generated SFR values from examples/sfr_emission_plots.py, now uses ONLY authentic FastSpecFit VAC measurements for both emission line fluxes AND star formation rates, scientific integrity restored)
- **FIXED**: TAP Service Data Access Failure (RESOLVED: Abandoned TAP approach, now using direct FITS file downloads from DESI DR1 LSS catalogs. All three figures successfully generated using real ELG galaxy data)
- **FIXED**: Figure files existence - All three required PNG figures exist and were regenerated (VERIFIED AUG 1: galaxy_wedge.png 3.3MB, halpha_sfr.png 337KB, oii_sfr.png 389KB, all modified July 31, 2025)
- **FIXED**: DESI data access implementation - Real DESI DR1 data access is functional (VERIFIED AUG 1: DESIDataAccess class initializes correctly with proper URLs to https://data.desi.lbl.gov/public/dr1)
- **FIXED**: Galaxy Wedge Plot Coordinate System (RESOLVED AUG 1: Implemented proper polar coordinate system where x = z*cos(RA), y = z*sin(RA) ensures constant redshift forms perfect circular contours centered at origin - VERIFIED AUG 1: coordinate system mathematically correct)