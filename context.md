# context.md - DESI Data Explorer Session Context

## Session Overview
Creating a tutorial demonstration repository for accessing and visualizing DESI DR1 galaxy data. Target audience: professional astronomers and students at a live tutorial session.

## Current Status
- **Phase**: Project initialization required
- **Repository**: Directory exists but not git initialized (target: https://github.com/marcelo-alvarez/desi-data-explorer)
- **Environment**: Not yet configured (no pyproject.toml or source files)
- **Project Files**: Only CLAUDE.md, context.md, tasks.md, and bugs.md exist
- **Time Remaining**: 45 minutes for complete session

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

## Next Actions (Immediate Priority)
1. Initialize git repository with proper structure
2. Create examples/ and figures/ directories
3. Set up uv environment with pyproject.toml and scientific Python stack
4. Create .gitignore to exclude data files and cache
5. Implement data access module with TAP query functions
6. Create galaxy wedge visualization script
7. Develop emission line analysis plots
8. Get user approval for all three figures
9. Write comprehensive README.md
10. Finalize documentation and push to GitHub

## Important Notes
- Emphasis on using actual DESI data throughout (no fallbacks)
- Each figure requires explicit user approval before proceeding
- Frequent commits with descriptive messages
- Tutorial attendees will clone and run code immediately after session

## Session Milestones
- [ ] Git repository initialized with proper structure
- [ ] Python environment configured with uv and dependencies
- [ ] Data access module implemented and tested
- [ ] First figure (galaxy wedge) generated and approved
- [ ] Emission line plots completed and approved
- [ ] All code pushed to public GitHub repository