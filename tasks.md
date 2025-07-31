# tasks.md - DESI Data Explorer Development Tasks

## Setup Phase
- [ ] Initialize git repository
- [ ] Create repository structure with examples/ and figures/ directories
- [ ] Set up Python environment with uv
- [ ] Create pyproject.toml with dependencies:
  - numpy
  - matplotlib
  - astropy
  - astroquery
  - pandas
  - scipy
  - tqdm
- [ ] Create .gitignore (exclude *.fits, *.csv, __pycache__, .venv)
- [ ] Write initial README.md with project description
- [ ] Commit and push initial setup

## Data Access Implementation
- [ ] Create `desi_data_access.py` module with:
  - [ ] TAP query function for NOIRLab
  - [ ] Galaxy catalog query with quality cuts
  - [ ] FastSpecFit VAC query function
  - [ ] Error handling for network issues
- [ ] Test queries with small samples (100 galaxies)
- [ ] Implement progress indicators for large queries
- [ ] Add docstrings with parameter descriptions
- [ ] Commit data access utilities

## Galaxy Wedge Visualization
- [ ] Implement `examples/galaxy_wedge_plot.py`:
  - [ ] Query 50,000 main survey galaxies
  - [ ] Calculate optimal projection plane
  - [ ] Convert RA/Dec/z to Cartesian coordinates
  - [ ] Create orthographic projection
  - [ ] Add color mapping by redshift
  - [ ] Include proper axis labels and title
- [ ] Generate initial wedge plot
- [ ] Get user approval for wedge visualization
- [ ] Save approved figure as `figures/galaxy_wedge.png`
- [ ] Commit wedge visualization code and figure

## Emission Line Analysis
- [ ] Implement `examples/sfr_emission_plots.py`:
  - [ ] Query galaxies with FastSpecFit measurements
  - [ ] Filter for reliable Halpha and OII detections
  - [ ] Create density scatter plot utilities
  - [ ] Implement log-scale with proper handling of zeros
- [ ] Generate Halpha vs SFR plot:
  - [ ] Use HALPHA_FLUX and SFR_HALPHA columns
  - [ ] Add 1:1 relation line
  - [ ] Include proper axis labels with units
- [ ] Get user approval for Halpha plot
- [ ] Save as `figures/halpha_sfr.png`
- [ ] Generate OII vs SFR plot:
  - [ ] Use OII_3727_FLUX and SFR_OII columns
  - [ ] Match styling with Halpha plot
  - [ ] Add appropriate redshift range note
- [ ] Get user approval for OII plot
- [ ] Save as `figures/oii_sfr.png`
- [ ] Commit emission line analysis and figures

## Documentation and Finalization
- [ ] Update README.md with:
  - [ ] Installation instructions using uv
  - [ ] Usage examples for both scripts
  - [ ] Description of output figures
  - [ ] DESI DR1 citation information
- [ ] Add inline comments to complex code sections
- [ ] Verify all scripts run in fresh environment
- [ ] Create final commit with any cleanup
- [ ] Push all changes to GitHub
- [ ] Confirm repository accessible at target URL

## Verification Checklist
- [ ] All three PNG figures approved by user
- [ ] Scripts use only real DESI DR1 data
- [ ] No data files included in repository
- [ ] Code runs on macOS with uv environment
- [ ] Repository publicly accessible on GitHub
- [ ] Total time under 45 minutes