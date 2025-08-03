# DESI Data Explorer

A demonstration repository created during a Claude Code tutorial session, showing how to access and visualize DESI Data Release 1 (DR1) galaxy data.

## Overview

This repository contains Python scripts that demonstrate basic visualization techniques for DESI DR1 galaxy data. The code was developed during a live tutorial to showcase AI-assisted development workflows and serves as an example of working with astronomical survey data.

## Development Process

### Planning Phase (Claude Desktop)

Before the live tutorial, a planning session was conducted using Claude Desktop to create the foundational project documents:

- **CLAUDE.md**: Project guidelines establishing key objectives, technical requirements, and constraints
- **tasks.md**: Detailed development checklist breaking down the work into phases
- **context.md**: Initial session context to maintain continuity between development sessions

Key planning decisions included:
- Using real DESI DR1 data via NERSC HTTPS or NOIRLab TAP services
- Creating two example scripts (galaxy wedge plot and emission line analysis)
- Generating three figures requiring user approval
- Targeting a 45-minute development session

### Development Phase (Claude Code)

The actual development used Claude Code with a structured `/run-dev-cycle` workflow consisting of:

1. **Start Session**: Load project context and establish baseline
2. **Audit Context**: Verify previous claims and update documentation
3. **Continue Work**: Execute development tasks
4. **Save Context**: Document believed accomplishments
5. **Final Audit**: Verify work and update status

This workflow used "BELIEVED COMPLETED" notation to distinguish between attempted work and verified accomplishments, creating clear handoffs between development cycles.

### Tutorial Timeline

- **Planning Session**: Created project structure and documentation templates
- **Live Tutorial**: 60 minutes with audience (basic setup and initial attempts)
- **Follow-up Development**: ~90 additional minutes to complete all objectives
- **Total Time**: ~2.5 hours from planning to final working code

## Features

The repository includes two example scripts:

1. **Galaxy Wedge Visualization**: A 2D projection showing the spatial distribution of ~50,000 galaxies
2. **Emission Line Analysis**: Scatter plots comparing emission line fluxes with star formation rates

## Requirements

- Python 3.9 or higher
- Scientific Python packages (see pyproject.toml)
- Internet connection for data downloads
- Approximately 5GB free disk space

## Installation

Clone the repository and install dependencies using uv:

```bash
git clone https://github.com/marcelo-alvarez/desi-data-explorer.git
cd desi-data-explorer
uv sync
```

Or using poetry:

```bash
poetry install
```

## Usage

### Galaxy Wedge Plot

```bash
uv run python examples/galaxy_wedge_plot.py
```

This script:
- Downloads DESI LSS clustering catalogs (~200MB)
- Loads data for LRG, ELG, and QSO galaxy types
- Creates a 2D wedge projection colored by redshift
- Saves the output to `figures/galaxy_wedge.png`

### Emission Line Analysis

```bash
uv run python examples/sfr_emission_plots.py
```

This script:
- Uses galaxy data from DESI catalogs
- Generates emission line flux measurements
- Creates scatter plots for Hα and [OII] versus star formation rate
- Saves outputs to `figures/halpha_sfr.png` and `figures/oii_sfr.png`

## Project Structure

```
desi-data-explorer/
├── README.md                    # This file
├── pyproject.toml              # Python dependencies
├── CLAUDE.md                   # Project guidelines from planning phase
├── tasks.md                    # Development checklist
├── context.md                  # Session context tracking
├── bugs.md                     # Issue tracking
├── src/
│   ├── __init__.py
│   └── desi_data_access.py    # Data access utilities
├── examples/
│   ├── galaxy_wedge_plot.py   # Wedge visualization script
│   └── sfr_emission_plots.py  # Emission line analysis
└── figures/                    # Output directory for plots
```

## Data Access Notes

The project uses DESI DR1 public data from:
- LSS clustering catalogs: `https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/`
- File sizes range from 100-500MB per catalog

First runs will take several minutes to download data. Subsequent runs use cached files from `/tmp/`.

## Performance Considerations

- Initial data download: 2-5 minutes depending on connection speed
- Galaxy query and loading: ~30 seconds for 50,000 objects
- Plot generation: ~10-20 seconds per figure

For tutorial or demonstration purposes, consider pre-downloading data files to avoid wait times during live sessions.

## Known Limitations

1. **Data Downloads**: Large file sizes can cause delays in live demonstrations
2. **Emission Line Data**: Uses synthetic measurements for tutorial efficiency
3. **Platform Testing**: Primarily tested on macOS; other platforms may require adjustments

## Tutorial Lessons

This project demonstrates several aspects of AI-assisted scientific software development:

### Technical Lessons
- Working with large astronomical datasets
- Creating scientific visualizations with matplotlib
- Organizing code for reusability
- Managing dependencies with modern Python tools

### Process Lessons
- The importance of realistic time estimates for data-intensive projects
- The value of structured development workflows (audit cycles)
- The difference between live demonstration needs and actual development
- How AI coding assistants handle iterative debugging and recovery

The development process illustrated common challenges in working with real survey data, including download performance, data format complexity, and the need for quality filtering.

## Development Workflow Documentation

The `/run-dev-cycle` slash-command workflow used in this project provides a structured approach to AI-assisted development:

- Separates work attempts from verified outcomes
- Creates audit trails for debugging
- Maintains context between sessions
- Enables systematic error detection and correction

This workflow proved particularly valuable when dealing with the complexity of astronomical data access and the need to maintain scientific accuracy throughout the development process.

## Citation

If you use this code for educational purposes, please acknowledge:

- DESI Collaboration et al. (2024) for the Data Release 1
- This repository: https://github.com/marcelo-alvarez/desi-data-explorer

## License

MIT License - see LICENSE file for details.

## Acknowledgments

Created as part of a Claude Code tutorial demonstration, with planning conducted in Claude Desktop. The visualizations use publicly available data from the Dark Energy Spectroscopic Instrument (DESI) Data Release 1.