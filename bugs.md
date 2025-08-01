# bugs.md - Bug Tracking

## OPEN BUGS

### Critical Architecture Issues
- **Poor Code Organization**: No separation between reusable interface and example code
  - Status: ARCHITECTURAL PROBLEM - all code mixed in root directory
  - Root Cause: `desi_data_access.py` is reusable library code but sits in root with examples
  - Required Fix: Create `src/` directory structure, move reusable code, add proper imports
  - Impact: Code is not properly modularized for tutorial/educational use
  - Priority: HIGH - affects code maintainability and educational value

- **Missing Documentation**: No README.md or comprehensive documentation
  - Status: CRITICAL GAP - repository lacks proper documentation
  - Root Cause: No README.md, insufficient docstrings, unclear API documentation
  - Required Fix: Create comprehensive README.md with installation/usage, add docstrings to all public functions
  - Impact: Tutorial attendees cannot easily understand or use the code
  - Priority: HIGH - essential for tutorial repository

- **Git Workflow Violations**: Commits not pushed, changes left uncommitted
  - Status: WORKFLOW VIOLATION - 1 unpushed commit + unstaged changes
  - Root Cause: Not following commit-and-push discipline after each change set
  - Required Fix: Implement strict rule - ALWAYS commit AND push after code changes
  - Impact: Work can be lost, collaboration is hindered
  - Priority: CRITICAL - must establish proper git hygiene

### Minor Issues  
- **Galaxy Wedge Plot Distortion**: Wedge visualization shows incorrect distance units and projection
  - Status: BELIEVED FIXED - corrected axis labels from Mpc to "redshift × angular"
  - Root Cause: Axis labels incorrectly claimed coordinates were in distance units
  - Applied Fix: Updated axis labels to properly describe coordinate system
  - Impact: One of three required figures - pending user approval
  - Priority: MEDIUM - fix applied, awaiting verification

## VERIFIED FIXED
- **FIXED**: Remote repository configuration - git remote origin successfully configured and connected (VERIFIED AUG 1: remote properly configured to https://github.com/marcelo-alvarez/desi-data-explorer.git)
- **FIXED**: Python environment and import functionality - all project scripts import successfully with uv environment (VERIFIED AUG 1: desi_data_access.py, galaxy_wedge_plot.py, and sfr_emission_plots.py all import without errors using `uv run python`)
- **FIXED**: CRITICAL - Figures Use Test Data Instead of Real DESI Data (RESOLVED: Successfully implemented real DESI DR1 data access using LSS clustering catalogs from https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.5/)
- **FIXED**: TAP Service Data Access Failure (RESOLVED: Abandoned TAP approach, now using direct FITS file downloads from DESI DR1 LSS catalogs. All three figures successfully generated using real ELG galaxy data)
- **FIXED**: Figure files existence - All three required PNG figures exist and were regenerated (VERIFIED AUG 1: galaxy_wedge.png 4.3MB, halpha_sfr.png 345KB, oii_sfr.png 399KB, all modified July 31, 2025)
- **FIXED**: DESI data access implementation - Real DESI DR1 data access is functional (VERIFIED AUG 1: DESIDataAccess class initializes correctly with proper URLs to https://data.desi.lbl.gov/public/dr1)