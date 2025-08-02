# bugs.md - Bug Tracking

## OPEN BUGS

### CRITICAL BLOCKING ISSUE - FASTSPECFIT DATA ACCESS PERFORMANCE
**Priority: CRITICAL - BLOCKS PROJECT COMPLETION**
**Discovery Date: August 2, 2025**
**Status: OPEN - BLOCKING DEPLOYMENT**

The FastSpecFit VAC data access is extremely inefficient, requiring download and processing of multi-gigabyte FITS files to extract emission line measurements for even small galaxy samples.

**CRITICAL Issues:**
- **CONFIRMED**: FastSpecFit VAC files are 1-7 GB each (12+ healpix files total)
- **CONFIRMED**: Script times out after 4+ minutes attempting to access ~5,000 galaxies
- **CONFIRMED**: Current approach downloads entire healpix files to find sparse matches
- **CONFIRMED**: Prevents completion of SFR emission line plots despite corrected code
- **CONFIRMED**: Violates tutorial time constraints - unusable for live educational sessions

**Performance Problems:**
- Downloads fastspec-iron-main-dark-nside1-hp01.fits (4.7 GB) for minimal data extraction
- Downloads fastspec-iron-main-dark-nside1-hp02.fits (7.1 GB) for minimal data extraction  
- Searches through millions of entries to find thousands of matches
- No efficient query mechanism for targeted TARGETID retrieval

**Required Solution:**
- MUST implement efficient FastSpecFit data access method
- MUST avoid downloading multi-gigabyte files for small samples
- MUST complete SFR plot generation within reasonable time (< 2 minutes)
- MUST maintain requirement for authentic DESI DR1 data (no mock data permitted)

**Impact:** BLOCKS repository deployment - cannot complete required SFR emission line plots
**Code Location:** `src/desi_data_access.py` query_fastspecfit_data() method

## VERIFIED FIXED
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