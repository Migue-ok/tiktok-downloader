# 🔍 Deployment Checker - Usage Guide

## Overview

The deployment checker helps ensure your code is ready for deployment by checking for uncommitted changes in your Git repository.

## Why Use It?

Deploying with uncommitted changes can lead to:
- **Version mismatches** - Production code differs from repository
- **Lost changes** - Uncommitted work not backed up
- **Debugging issues** - Hard to track which version is deployed
- **Team confusion** - Others can't see your latest changes

## Quick Start

### Check Before Deployment

```bash
# Linux/Mac
./check_deployment.sh

# Windows
check_deployment.bat

# Python (all platforms)
python check_deployment.py
```

### Expected Output

#### ✅ Clean Repository (Ready to Deploy)
```
============================================================
🚀 TikTok Downloader - Pre-Deployment Check
============================================================

✅ No uncommitted changes detected. Safe to proceed.
✅ All required dependencies are installed.

============================================================
✅ All checks passed! Ready for deployment
============================================================
```

#### ❌ Uncommitted Changes Detected
```
============================================================
🚀 TikTok Downloader - Pre-Deployment Check
============================================================

❌ Uncommitted changes detected!

The following files have uncommitted changes:
M app.py
M README.md
?? new_file.py

============================================================
Options:
  1. Commit changes: git add . && git commit -m 'Your message'
  2. Stash changes: git stash
  3. Proceed anyway: Use --force flag
============================================================

❌ Deployment check FAILED: Uncommitted changes detected
   Commit your changes or use --force to proceed anyway
============================================================
```

## Resolution Options

### Option 1: Commit Your Changes (Recommended)

```bash
# Add all changes
git add .

# Or add specific files
git add app.py README.md

# Commit with a descriptive message
git commit -m "Add new feature: video quality selector"

# Push to repository
git push origin main

# Now run the checker again
python check_deployment.py
```

### Option 2: Stash Your Changes

Use this when you have work-in-progress that you don't want to commit yet:

```bash
# Stash uncommitted changes
git stash save "Work in progress on feature X"

# Deploy
python check_deployment.py

# After deployment, restore your changes
git stash pop
```

### Option 3: Force Deployment (Use with Caution)

Only use this when you're certain the uncommitted changes don't affect deployment:

```bash
# Force deployment despite uncommitted changes
python check_deployment.py --force

# Or
./check_deployment.sh -f
```

**⚠️ Warning:** Forcing deployment with uncommitted changes means:
- Your deployed code won't match your repository
- Other developers won't see your latest changes
- You risk losing uncommitted work if something goes wrong

## Integration with CI/CD

### GitHub Actions Example

```yaml
name: Deploy

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Check for uncommitted changes
        run: python check_deployment.py
      
      - name: Deploy to production
        run: |
          # Your deployment commands here
          heroku push main
```

### Pre-commit Hook

Add this to `.git/hooks/pre-push`:

```bash
#!/bin/bash
echo "Running pre-deployment checks..."
python check_deployment.py
if [ $? -ne 0 ]; then
    echo "Pre-deployment checks failed. Push cancelled."
    exit 1
fi
```

## Troubleshooting

### "Git not found"
- Install Git: https://git-scm.com/downloads
- Make sure Git is in your system PATH

### "Not a git repository"
- Initialize Git: `git init`
- Or clone from repository: `git clone <url>`

### "Python not found"
- Install Python 3.8+: https://python.org
- Make sure Python is in your system PATH

### Script permission denied (Linux/Mac)
```bash
chmod +x check_deployment.sh
```

## Best Practices

1. **Always run before deployment** - Make it a habit
2. **Commit meaningful changes** - Don't force unless necessary
3. **Write clear commit messages** - Helps track what was deployed
4. **Push to remote** - Ensure backup of your changes
5. **Use stash for WIP** - Keep your commits clean

## What Gets Checked

The deployment checker verifies:

1. **Git Status**
   - Modified files (M)
   - New files (??)
   - Deleted files (D)
   - Renamed files (R)
   - Files with conflicts (U)

2. **Dependencies** (Python version only)
   - Checks if Flask is installed
   - Checks if yt-dlp is installed

## Exit Codes

- `0` - All checks passed, safe to deploy
- `1` - Checks failed, fix issues before deployment

## Examples

### Example 1: Normal Workflow

```bash
# Make changes
vim app.py

# Test locally
python app.py

# Check deployment readiness
python check_deployment.py
# ❌ Uncommitted changes detected!

# Commit changes
git add app.py
git commit -m "Fix video download bug"

# Check again
python check_deployment.py
# ✅ All checks passed!

# Deploy
git push heroku main
```

### Example 2: Emergency Hotfix

```bash
# Make critical fix
vim app.py

# Need to deploy immediately
python check_deployment.py --force
# ⚠️ Proceeding despite uncommitted changes

# Deploy
git push heroku main

# Don't forget to commit later!
git add app.py
git commit -m "Hotfix: critical security patch"
git push origin main
```

## Support

If you encounter issues with the deployment checker:

1. Check the error message carefully
2. Verify Git is installed and working
3. Ensure you're in the project directory
4. Check file permissions (Linux/Mac)

For more help, open an issue on GitHub.

---

**Remember:** A clean repository is a happy repository! 🎉
