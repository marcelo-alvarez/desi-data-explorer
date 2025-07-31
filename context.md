# context.md - DESI Data Explorer Session Context

## Session Overview
Creating a tutorial demonstration repository for accessing and visualizing DESI DR1 galaxy data. Target audience: professional astronomers and students at a live tutorial session.

## Current Status
- **Phase**: Initial setup completed, moving to implementation phase
- **Repository**: Git repository initialized with proper structure and first commit created
- **Environment**: Python environment configured with uv and pyproject.toml with scientific dependencies
- **Project Files**: Core infrastructure in place including data access module
- **Progress**: Completed all high-priority setup tasks from todo list
- **Time Remaining**: ~30-35 minutes for visualization implementation

## Key Requirements Confirmed
1. Use real DESI DR1 data via NERSC HTTPS or NOIRLab TAP (no mock data)
2. Create two example scripts:
   - Galaxy wedge plot showing ~50,000 galaxies across full redshift range
   - Emission line (Halpha, OII) vs SFR density scatter plots
3. Generate three PNG figures requiring user approval
4. Use uv or poetry for environment management (prefer uv)
5. Optimize for macOS compatibility
6. Include only source code and PNG figures in repo (no data files)

## Technical Decisions
- **Data Access**: Use NOIRLab TAP service via astroquery for efficient queries
- **Galaxy Selection**: Main survey galaxies with ZWARN=0 and SPECTYPE='GALAXY'
- **Visualization**: Matplotlib for all plots with scientific styling
- **FastSpecFit VAC**: Access via TAP join for emission line measurements

## Next Actions (For Future Sessions)
1. **Immediate Priority**: Implement galaxy wedge visualization script
   - Create examples/galaxy_wedge_plot.py with 50k galaxy sample
   - Calculate optimal projection plane for minimal angular spread
   - Generate orthographic projection with redshift color mapping
   - Test and get user approval for wedge figure
   - **COMMIT AND PUSH** wedge visualization to remote
2. **Secondary Priority**: Develop emission line analysis
   - Create examples/sfr_emission_plots.py
   - Implement Halpha vs SFR density scatter plots
   - Add OII vs SFR visualization with proper redshift ranges
   - Get user approval for both emission line figures
   - **COMMIT AND PUSH** emission line analysis to remote
3. **Documentation Phase**: 
   - Write comprehensive README.md with installation/usage instructions
   - Add inline code comments and documentation
   - Final testing in fresh environment
   - **COMMIT AND PUSH** documentation updates to remote
4. **Deployment**: Ensure all changes pushed to GitHub at target URL

## Technical Notes for Next Session
- Data access module uses NOIRLab TAP service with proven query patterns
- Target 50,000 galaxies with full redshift coverage (0 < z < 1.5)
- All visualizations should use matplotlib with scientific styling
- Each figure requires explicit user approval before proceeding
- **CRITICAL**: Commit AND push to remote after each major milestone
- Maintain frequent commits with descriptive messages
- Remote repository target: https://github.com/marcelo-alvarez/desi-data-explorer

## Important Notes
- Emphasis on using actual DESI data throughout (no fallbacks)
- Each figure requires explicit user approval before proceeding
- Frequent commits with descriptive messages
- Tutorial attendees will clone and run code immediately after session

## Session Milestones
- [x] Git repository initialized with proper structure
- [x] Python environment configured with uv and dependencies
- [x] Data access module implemented (desi_data_access.py with NOIRLab TAP queries)
- [ ] First figure (galaxy wedge) generated and approved
- [ ] Emission line plots completed and approved
- [ ] All code pushed to public GitHub repository

## Work Believed Accomplished This Session

### Infrastructure Setup (Completed)
1. **Git Repository**: Initialized git repository with proper structure
2. **Directory Structure**: Created examples/ and figures/ directories  
3. **Python Environment**: Set up pyproject.toml with uv and scientific Python dependencies:
   - numpy, matplotlib, astropy, astroquery, pandas, scipy, tqdm
4. **Git Configuration**: Created comprehensive .gitignore excluding data files and cache
5. **Initial Commit**: Created first commit with descriptive message

### Data Access Implementation (Completed)
1. **Core Module**: Implemented desi_data_access.py with DESIDataAccess class
2. **TAP Integration**: Connected to NOIRLab TAP service at datalab.noirlab.edu/tap
3. **Galaxy Queries**: Added query_galaxies() method with quality filters:
   - SPECTYPE='GALAXY', ZWARN=0, SURVEY='main'
   - Configurable redshift, RA, Dec ranges
   - Progress indicators and error handling
4. **Emission Line Support**: Implemented query_fastspecfit_data() for VAC access
5. **Quality Samples**: Added get_quality_sample() with SNR filtering
6. **Test Framework**: Included test_data_access() function for validation