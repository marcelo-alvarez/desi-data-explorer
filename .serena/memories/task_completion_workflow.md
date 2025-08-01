# Task Completion Workflow

## After Each Major Task
1. **Test the implementation**:
   - Run the script to verify it works
   - Check that figures are generated correctly
   - Verify data queries return actual DESI DR1 data

2. **Get user approval** (CRITICAL):
   - Show generated figures to user for approval
   - Each of the 3 PNG files requires explicit user approval
   - Do not proceed to next task without approval

3. **Commit and push**:
   - Create atomic commit with clear message
   - Push to remote repository immediately
   - Follow commit message examples from CLAUDE.md

## Testing Protocol
- Test each script with small data samples first
- Verify network connectivity and query performance
- Ensure figures are generated correctly before committing
- Code must run successfully in fresh environment

## Quality Checks Before Final Commit
- All data queries return actual DESI DR1 data (no mock data)
- Figures are scientifically accurate and publication-ready
- Code runs successfully in fresh uv environment
- Documentation is clear for tutorial attendees
- Repository structure matches planned layout

## No Standard Linting/Formatting
- Project does not specify linting tools (ruff, black, etc.)
- Focus on code clarity and scientific accuracy
- Follow existing code patterns in desi_data_access.py