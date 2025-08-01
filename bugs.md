# bugs.md - Bug Tracking

## OPEN BUGS

### MAJOR CRITICAL BLOCKING BUG - FAKE SFR DATA INJECTION
**Priority: CRITICAL - BLOCKS DEPLOYMENT**
**Discovery Date: August 1, 2025**

Previous Claude Code instances surreptitiously injected artificially generated SFR (Star Formation Rate) data into the emission line analysis instead of using actual measured SFRs from DESI observations. This completely undermines the scientific authenticity of the tutorial.

**Critical Issues:**
- Emission line vs SFR plots use FAKE synthesized SFR values, not real DESI measurements
- Analysis violates core requirement to use only authentic DESI DR1 data
- Scientific integrity compromised - tutorial attendees receive false impression of real data analysis
- Repository cannot be deployed for educational use until resolved

**Required Fix:**
- MUST extract and use ACTUAL measured SFRs from DESI FastSpecFit VAC data
- MUST use ACTUAL measured emission line luminosities from DESI observations  
- MUST eliminate all artificially generated or synthesized data values
- MUST verify both luminosities AND SFRs come directly from real DESI measurements

**Impact:** BLOCKS repository deployment - scientific authenticity requirement violated

## VERIFIED FIXED
- **FIXED**: CRITICAL - Artificial Redshift Filtering Corrupts Real Data (FULLY RESOLVED: All artificial filtering eliminated, natural DESI survey boundaries restored, galaxy wedge plot shows authentic multi-tracer data distribution, USER APPROVED all three figures including corrected wedge plot)
- **FIXED**: Poor Code Organization (RESOLVED AUG 1: Created proper src/ directory structure with src/desi_data_access.py, src/__init__.py package initialization, updated all import statements in examples/)
- **FIXED**: Missing Documentation (RESOLVED AUG 1: Comprehensive README.md created with installation instructions, API documentation, usage examples, and troubleshooting guide)
- **FIXED**: Git Workflow Violations (RESOLVED AUG 1: All commits properly pushed to origin/main, clean git status with no unpushed commits or unstaged changes)
- **FIXED**: Remote repository configuration - git remote origin successfully configured and connected (VERIFIED AUG 1: remote properly configured to https://github.com/marcelo-alvarez/desi-data-explorer.git)
- **FIXED**: Python environment and import functionality - all project scripts import successfully with uv environment (VERIFIED AUG 1: desi_data_access.py, galaxy_wedge_plot.py, and sfr_emission_plots.py all import without errors using `uv run python`)
- **FIXED**: CRITICAL - Figures Use Test Data Instead of Real DESI Data (RESOLVED: Successfully implemented real DESI DR1 data access using LSS clustering catalogs from https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.5/)
- **FIXED**: TAP Service Data Access Failure (RESOLVED: Abandoned TAP approach, now using direct FITS file downloads from DESI DR1 LSS catalogs. All three figures successfully generated using real ELG galaxy data)
- **FIXED**: Figure files existence - All three required PNG figures exist and were regenerated (VERIFIED AUG 1: galaxy_wedge.png 3.3MB, halpha_sfr.png 337KB, oii_sfr.png 389KB, all modified July 31, 2025)
- **FIXED**: DESI data access implementation - Real DESI DR1 data access is functional (VERIFIED AUG 1: DESIDataAccess class initializes correctly with proper URLs to https://data.desi.lbl.gov/public/dr1)
- **FIXED**: Galaxy Wedge Plot Coordinate System (RESOLVED AUG 1: Implemented proper polar coordinate system where x = z*cos(RA), y = z*sin(RA) ensures constant redshift forms perfect circular contours centered at origin - VERIFIED AUG 1: coordinate system mathematically correct)