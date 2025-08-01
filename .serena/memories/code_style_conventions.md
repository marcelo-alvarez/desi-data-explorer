# Code Style and Conventions

## General Guidelines
- Clear, professional-level documentation for astronomers
- Modular functions with type hints where appropriate
- Error handling for network requests and data queries
- Progress indicators for long-running operations

## Code Organization
- **DESIDataAccess class**: Central data access with methods:
  - `query_galaxies()`: Main survey galaxy queries with quality filters
  - `query_fastspecfit_data()`: Emission line measurements from VAC
  - `get_quality_sample()`: Apply SNR and quality filtering
- TAP queries use NOIRLab service at datalab.noirlab.edu/tap
- Galaxy selection: SPECTYPE='GALAXY', ZWARN=0, SURVEY='main'

## Visualization Standards
- Use matplotlib with scientific styling
- Color by redshift or galaxy properties
- Proper axis labels with units
- Density scatter plots for large datasets
- Log-scale handling with appropriate zero treatment

## Data Processing
- Target ~50,000 galaxies for visualization
- Prioritize redshift coverage over total count
- Filter for reliable measurements: FLUX_IVAR > 0
- Join zpix catalog with FastSpecFit VAC on TARGETID