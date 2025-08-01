# Suggested Commands for DESI Data Explorer

## Environment Setup
```bash
# Initialize uv environment (if not done)
uv init

# Install dependencies
uv sync

# Activate virtual environment
source .venv/bin/activate  # or use uv run
```

## Development Commands
```bash
# Run visualization scripts
uv run examples/galaxy_wedge_plot.py
uv run examples/sfr_emission_plots.py

# Test data access
uv run -m desi_data_access  # Run test_data_access()

# Python interactive with environment
uv run python
```

## Git Workflow
```bash
# Check status
git status

# Stage and commit changes
git add .
git commit -m "Descriptive commit message"

# Push to remote
git push origin main
```

## Darwin System Commands
```bash
# List files
ls -la

# Find files
find . -name "*.py"

# Search in files
grep -r "pattern" .

# Change directory
cd examples/

# View file contents
cat filename.py
less filename.py
```

## Testing and Validation
```bash
# Test with small data sample
uv run python -c "from desi_data_access import test_data_access; test_data_access()"

# Verify figures generated
ls -la figures/

# Check file sizes
du -h figures/*.png
```