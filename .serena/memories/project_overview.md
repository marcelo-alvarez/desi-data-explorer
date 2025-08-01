# DESI Data Explorer Project Overview

## Purpose
This repository demonstrates accessing and visualizing DESI Data Release 1 (DR1) galaxy data for a tutorial audience of professional astronomers and students. The project emphasizes using real DESI data via NERSC HTTPS or NOIRLab TAP services, avoiding mock data entirely.

## Key Objectives
1. Create a well-documented repository at https://github.com/marcelo-alvarez/desi-data-explorer
2. Implement two example scripts using real DESI DR1 data:
   - 2D wedge visualization of ~50,000 main survey galaxies
   - Density-scatter plots of emission line luminosity vs star formation rate
3. Generate three approved PNG figures for the repository
4. Complete development within ~45 minutes including file transfers

## Current Status
- Infrastructure setup completed (git repo, uv environment, pyproject.toml)
- Data access module implemented (desi_data_access.py with DESIDataAccess class)
- Next phase: Implement visualization scripts and generate figures