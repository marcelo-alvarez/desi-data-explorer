# CLAUDE.md - DESI Data Explorer Development Documentation

## Project Completion Summary
This repository was successfully developed during a live Claude Code tutorial session, demonstrating AI-assisted astronomical software development. The project achieved all objectives and generated three scientifically accurate visualizations using authentic DESI DR1 data.

## Completed Objectives ✅
1. ✅ Created well-documented repository at https://github.com/marcelo-alvarez/desi-data-explorer
2. ✅ Implemented two example scripts using real DESI DR1 data:
   - 2D wedge visualization of ~50,000 main survey galaxies (multi-tracer: LRG, ELG, QSO)
   - Density-scatter plots of emission line luminosity vs star formation rate
3. ✅ Generated three approved PNG figures for the repository
4. ✅ Completed development with all major milestones achieved

## Development Session Highlights
- **Real-time AI Development**: Complete codebase developed with Claude Code assistance
- **Scientific Authenticity**: All visualizations use genuine DESI DR1 observations
- **Professional Standards**: Established proper src/ package structure and documentation
- **Bug Resolution**: Successfully resolved critical data filtering and SFR calculation issues

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

## Final Achievement Status
✅ **All Development Completed Successfully**
- Repository setup and environment configuration
- DESI data access implementation using direct FITS downloads
- Galaxy wedge visualization with multi-tracer data (LRG, ELG, QSO)
- Emission line analysis with authentic FastSpecFit measurements  
- Professional documentation and code organization
- User approval obtained for all three generated figures

## Constraints Successfully Met ✅
- ✅ NO mock data - used only real DESI DR1 observations throughout
- ✅ NO data files in repository - only source code and PNG figures committed
- ✅ User approval obtained for all three figures before finalization
- ✅ Development session completed with all objectives achieved

## Repository Status: DEPLOYMENT READY
This repository now serves as a complete example of AI-assisted astronomical software development, ready for educational use and further research applications.