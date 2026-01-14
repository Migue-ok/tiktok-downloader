#!/usr/bin/env python3
"""
Pre-deployment checker for TikTok Downloader
Verifies that there are no uncommitted changes before deployment
"""
import subprocess
import sys
import os

def check_git_status():
    """Check if there are uncommitted changes in the repository"""
    try:
        # Check if we're in a git repository
        result = subprocess.run(
            ['git', 'rev-parse', '--git-dir'],
            capture_output=True,
            text=True,
            check=False
        )
        
        if result.returncode != 0:
            print("⚠️  Not a git repository. Skipping git checks.")
            return True
        
        # Check for uncommitted changes
        result = subprocess.run(
            ['git', 'status', '--porcelain'],
            capture_output=True,
            text=True,
            check=True
        )
        
        git_status_output = result.stdout.strip()
        
        if git_status_output:
            print("❌ Uncommitted changes detected!")
            print("\nThe following files have uncommitted changes:")
            print(git_status_output)
            print("\n" + "="*60)
            print("Options:")
            print("  1. Commit changes: git add . && git commit -m 'Your message'")
            print("  2. Stash changes: git stash")
            print("  3. Proceed anyway: Use --force flag")
            print("="*60)
            return False
        
        print("✅ No uncommitted changes detected. Safe to proceed.")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Error checking git status: {e}")
        return False
    except FileNotFoundError:
        print("⚠️  Git not found. Install git or skip this check.")
        return False

def check_dependencies():
    """Check if all required dependencies are installed"""
    required_modules = ['flask', 'yt_dlp']
    missing_modules = []
    
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            missing_modules.append(module)
    
    if missing_modules:
        print(f"❌ Missing dependencies: {', '.join(missing_modules)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    print("✅ All required dependencies are installed.")
    return True

def main():
    """Main deployment checker"""
    print("\n" + "="*60)
    print("🚀 TikTok Downloader - Pre-Deployment Check")
    print("="*60 + "\n")
    
    force_mode = '--force' in sys.argv or '-f' in sys.argv
    
    # Check git status
    git_ok = check_git_status()
    
    # Check dependencies
    deps_ok = check_dependencies()
    
    print("\n" + "="*60)
    
    if not git_ok and not force_mode:
        print("❌ Deployment check FAILED: Uncommitted changes detected")
        print("   Commit your changes or use --force to proceed anyway")
        print("="*60 + "\n")
        sys.exit(1)
    
    if not deps_ok:
        print("❌ Deployment check FAILED: Missing dependencies")
        print("="*60 + "\n")
        sys.exit(1)
    
    if force_mode and not git_ok:
        print("⚠️  Proceeding with deployment despite uncommitted changes (forced)")
    else:
        print("✅ All checks passed! Ready for deployment")
    
    print("="*60 + "\n")
    return 0

if __name__ == '__main__':
    sys.exit(main())
