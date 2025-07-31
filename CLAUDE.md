# CLAUDE.md - DESI Data Explorer Project Guidelines

## Project Overview
This repository demonstrates accessing and visualizing DESI Data Release 1 (DR1) galaxy data for a tutorial audience of professional astronomers and students. The project emphasizes using real DESI data via NERSC HTTPS or NOIRLab TAP services, avoiding mock data entirely.

## Key Objectives
1. Create a well-documented repository at https://github.com/marcelo-alvarez/desi-data-explorer
2. Implement two example scripts using real DESI DR1 data:
   - 2D wedge visualization of ~50,000 main survey galaxies
   - Density-scatter plots of emission line luminosity vs star formation rate
3. Generate three approved PNG figures for the repository
4. Complete development within ~45 minutes including file transfers

## Technical Requirements

### Environment Setup
- Use `uv` or `poetry` for dependency management (prefer `uv` for speed)
- Target compatibility with macOS (M1/M2 MacBook Air)
- Python 3.9+ with scientific stack (numpy, matplotlib, astropy, astroquery)

### Data Access Guidelines
- Fetch data programmatically via NERSC HTTPS or NOIRLab TAP
- No authentication required for DESI DR1 public data
- Target ~50,000 galaxies for visualization (prioritize redshift coverage over total count)
- Use FastSpecFit VAC for emission line measurements

### Code Standards
- Clear, professional-level documentation for astronomers
- Modular functions with type hints where appropriate
- Error handling for network requests and data queries
- Progress indicators for long-running operations

## Repository Structure
```
desi-data-explorer/
├── README.md                 # Project overview and usage instructions
├── pyproject.toml           # Project dependencies (uv/poetry)
├── examples/
│   ├── galaxy_wedge_plot.py    # 2D visualization script
│   └── sfr_emission_plots.py   # Halpha/OII vs SFR plots
├── figures/
│   ├── galaxy_wedge.png        # Output visualization
│   ├── halpha_sfr.png         # Halpha-SFR relationship
│   └── oii_sfr.png            # OII-SFR relationship
└── .gitignore               # Exclude data files, cache
```

## Development Workflow

### Commit Strategy
- Atomic commits with clear messages
- Push to remote after each significant milestone
- Example commit sequence:
  1. "Initial repository setup with uv"
  2. "Add DESI data access utilities"
  3. "Implement galaxy wedge visualization"
  4. "Add emission line analysis functions"
  5. "Generate approved figures"

### Testing Protocol
- Test each script with small data samples first
- Verify network connectivity and query performance
- Ensure figures are generated correctly before committing

## Data Processing Notes

### Galaxy Wedge Visualization
- Query main survey galaxies with `SPECTYPE='GALAXY'` and `ZWARN=0`
- Use redshift as radial coordinate (0 < z < ~1.5 for DESI)
- Optimize projection plane to minimize angular spread
- Orthographic projection preserving azimuthal angles
- Color by redshift or galaxy properties

### Emission Line Analysis
- Join `zpix` catalog with FastSpecFit VAC on TARGETID
- Filter for reliable measurements: `FLUX_IVAR > 0`
- Use pre-computed SFR values from VAC
- Create density scatter plots with appropriate scaling

## Quality Checks
- All data queries must return actual DESI DR1 data
- Figures must be scientifically accurate and publication-ready
- Code must run successfully in fresh environment
- Documentation must be clear for tutorial attendees

## Time Management
- 0-10 min: Repository setup and environment configuration
- 10-25 min: Implement data access and first visualization
- 25-35 min: Complete emission line analysis
- 35-40 min: Generate and verify all figures
- 40-45 min: Final documentation and push to GitHub

## Important Constraints
- NO mock data - use only real DESI DR1 observations
- NO data files in repository - only source code and PNG figures
- MUST have user approval for all three figures before finalizing
- MUST complete within 45-minute session