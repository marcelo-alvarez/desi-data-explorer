# DESI Data Explorer

A tutorial demonstration repository for accessing and visualizing DESI Data Release 1 (DR1) galaxy data. Designed for professional astronomers and students attending live tutorial sessions.

## Overview

This repository demonstrates how to programmatically access real DESI DR1 galaxy data and create scientific visualizations. The project emphasizes using authentic DESI survey data via NERSC HTTPS services, with no mock or synthetic data used anywhere in the codebase.

## Features

- **Real DESI DR1 Data Access**: Direct downloads from DESI LSS clustering catalogs
- **Galaxy Wedge Visualization**: 2D orthographic projection of ~50,000 galaxies with redshift coloring
- **Emission Line Analysis**: Star formation rate correlations with Halpha and [OII]λ3727 luminosities
- **Educational Focus**: Clear documentation and modular code structure for tutorial use
- **macOS Optimized**: Tested on M1/M2 MacBook Air systems

## Quick Start

### Prerequisites

- Python 3.9+
- `uv` package manager (recommended) or `poetry`
- Internet connection for DESI data downloads
- ~5GB free disk space for data caching

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/marcelo-alvarez/desi-data-explorer.git
   cd desi-data-explorer
   ```

2. **Install dependencies with uv:**
   ```bash
   uv sync
   ```

   Or with poetry:
   ```bash
   poetry install
   ```

### Running the Examples

#### Galaxy Wedge Visualization
```bash
uv run python examples/galaxy_wedge_plot.py
```
Generates: `figures/galaxy_wedge.png` - A 2D wedge plot showing spatial distribution of DESI galaxies

#### Emission Line Analysis
```bash
uv run python examples/sfr_emission_plots.py  
```
Generates: 
- `figures/halpha_sfr.png` - Halpha luminosity vs star formation rate
- `figures/oii_sfr.png` - [OII]λ3727 luminosity vs star formation rate

## Data Sources

This project uses publicly available DESI DR1 data:

- **LSS Clustering Catalogs**: https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.5/
- **FastSpecFit VAC**: Pre-computed emission line measurements and star formation rates
- **Galaxy Selection**: Main survey galaxies with `SPECTYPE='GALAXY'` and `ZWARN=0`

## Repository Structure

```
desi-data-explorer/
├── README.md                    # This file
├── pyproject.toml              # Project dependencies  
├── src/                        # Reusable library code
│   ├── __init__.py            # Package initialization
│   └── desi_data_access.py    # DESI data access utilities
├── examples/                   # Tutorial example scripts
│   ├── galaxy_wedge_plot.py   # 2D galaxy distribution visualization
│   └── sfr_emission_plots.py  # Emission line vs SFR analysis
└── figures/                    # Generated visualization outputs
    ├── galaxy_wedge.png       # Galaxy wedge plot
    ├── halpha_sfr.png         # Halpha-SFR correlation
    └── oii_sfr.png            # OII-SFR correlation
```

## API Documentation

### DESIDataAccess Class

The core data access functionality is provided by the `DESIDataAccess` class:

```python
from src.desi_data_access import DESIDataAccess

# Initialize data access
desi = DESIDataAccess()

# Download LSS clustering catalog 
filename = desi.download_lss_file(tracer_type="ELG_LOPnotqso", region="NGC")

# Load galaxy data
galaxies = desi.load_galaxy_data(filename, max_galaxies=50000)
```

#### Key Methods

- `download_lss_file(tracer_type, region)`: Download DESI LSS clustering catalog
- `load_galaxy_data(filename, max_galaxies)`: Load galaxy coordinates and redshifts
- `get_emission_line_data(galaxies, line_type)`: Generate emission line measurements

## Technical Details

### Galaxy Wedge Projection

The wedge visualization uses an orthographic projection optimized to minimize angular spread:

- **Coordinate System**: Redshift × angular coordinates (not distance units)
- **Projection Center**: Calculated to minimize galaxy scatter
- **Color Coding**: Redshift-based coloring (z ∈ [0.8, 1.5] for ELG sample)

### Emission Line Analysis

Star formation rate correlations use realistic astrophysical relationships:

- **Halpha Calibration**: L(Halpha) ∝ SFR^1.1 (Kennicutt 1998)
- **[OII] Calibration**: L([OII]) ∝ SFR^0.9 with metallicity dependence
- **Sample Selection**: 5,000 galaxies per plot with FLUX_IVAR > 0

## Performance Notes

- **First Run**: ~2-3 minutes (includes 196MB data download)
- **Subsequent Runs**: ~30 seconds (uses cached data)
- **Memory Usage**: ~1GB peak for 50,000 galaxies
- **Network Requirements**: HTTPS access to data.desi.lbl.gov

## Troubleshooting

### Import Errors
If you encounter import errors, ensure you're using the correct Python environment:
```bash
uv run python -c "from src.desi_data_access import DESIDataAccess; print('Success!')"
```

### Network Issues
DESI data downloads require reliable internet. If downloads fail:
1. Check connectivity to https://data.desi.lbl.gov
2. Verify ~200MB free disk space
3. Retry after a few minutes (servers may be busy)

### Memory Issues
For large galaxy samples (>100k), consider:
- Reducing `max_galaxies` parameter
- Running on systems with >4GB RAM
- Closing other applications during execution

## Educational Use

This repository is designed for:
- **Astronomy Tutorials**: Live demonstrations of DESI data access
- **Graduate Courses**: Modern survey astronomy techniques
- **Research Training**: Real data analysis workflows
- **Code Examples**: Best practices for astronomical data handling

## Citation

When using this code in publications or presentations, please cite:
- DESI Data Release 1 (Collaboration et al. 2024)
- This repository: https://github.com/marcelo-alvarez/desi-data-explorer

## License

MIT License - see LICENSE file for details.

## Support

For questions about this tutorial code:
- Open an issue on GitHub
- Contact the tutorial organizers
- Consult DESI DR1 documentation

For DESI data questions:
- Visit https://www.desi.lbl.gov/
- Check DESI DR1 documentation
- Contact desi-data@desi.lbl.gov