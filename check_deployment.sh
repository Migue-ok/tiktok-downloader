#!/bin/bash
# Pre-deployment checker for TikTok Downloader
# Verifies that there are no uncommitted changes before deployment

set -e

echo ""
echo "============================================================"
echo "🚀 TikTok Downloader - Pre-Deployment Check"
echo "============================================================"
echo ""

FORCE_MODE=false

# Check for --force flag
for arg in "$@"; do
    if [ "$arg" == "--force" ] || [ "$arg" == "-f" ]; then
        FORCE_MODE=true
    fi
done

# Check if git is available
if ! command -v git &> /dev/null; then
    echo "⚠️  Git not found. Skipping git checks."
    GIT_OK=true
else
    # Check if we're in a git repository
    if ! git rev-parse --git-dir &> /dev/null; then
        echo "⚠️  Not a git repository. Skipping git checks."
        GIT_OK=true
    else
        # Check for uncommitted changes
        if [ -n "$(git status --porcelain)" ]; then
            echo "❌ Uncommitted changes detected!"
            echo ""
            echo "The following files have uncommitted changes:"
            git status --short
            echo ""
            echo "============================================================"
            echo "Options:"
            echo "  1. Commit changes: git add . && git commit -m 'Your message'"
            echo "  2. Stash changes: git stash"
            echo "  3. Proceed anyway: Use --force flag"
            echo "============================================================"
            GIT_OK=false
        else
            echo "✅ No uncommitted changes detected. Safe to proceed."
            GIT_OK=true
        fi
    fi
fi

# Check if Python is available
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo "❌ Python not found. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python is installed."

echo ""
echo "============================================================"

if [ "$GIT_OK" = false ] && [ "$FORCE_MODE" = false ]; then
    echo "❌ Deployment check FAILED: Uncommitted changes detected"
    echo "   Commit your changes or use --force to proceed anyway"
    echo "============================================================"
    echo ""
    exit 1
fi

if [ "$FORCE_MODE" = true ] && [ "$GIT_OK" = false ]; then
    echo "⚠️  Proceeding with deployment despite uncommitted changes (forced)"
else
    echo "✅ All checks passed! Ready for deployment"
fi

echo "============================================================"
echo ""

exit 0
