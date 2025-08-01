# Technology Stack

## Language & Environment
- Python 3.9+ 
- Dependency management: `uv` (preferred) or `poetry`
- Target platform: macOS (M1/M2 MacBook Air)

## Core Dependencies
- **numpy>=1.21.0**: Numerical computing
- **matplotlib>=3.5.0**: Plotting and visualization
- **astropy>=5.0.0**: Astronomy-specific data structures and utilities
- **astroquery>=0.4.6**: Querying astronomical databases (NOIRLab TAP)
- **pandas>=1.5.0**: Data manipulation and analysis
- **scipy>=1.9.0**: Scientific computing
- **tqdm>=4.64.0**: Progress bars

## Data Access
- NOIRLab TAP service via astroquery
- DESI DR1 public data (no authentication required)
- FastSpecFit VAC for emission line measurements

## Project Structure
```
desi-data-explorer/
├── pyproject.toml           # uv/poetry dependencies
├── desi_data_access.py      # Data access utilities
├── examples/                # Visualization scripts
│   ├── galaxy_wedge_plot.py
│   └── sfr_emission_plots.py
└── figures/                 # Output PNG files
```