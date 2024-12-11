"""
Script to build and publish the package to PyPI.
"""

import subprocess
import sys
from pathlib import Path

def run_command(command: str) -> None:
    """Run a shell command and exit if it fails."""
    try:
        subprocess.run(command.split(), check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(e)
        sys.exit(1)

def main():
    # Clean up previous builds
    print("Cleaning up previous builds...")
    run_command("rm -rf dist build *.egg-info")

    # Run tests
    print("Running tests...")
    run_command("pytest tests/")

    # Build the package
    print("Building package...")
    run_command("python -m build")

    # Upload to PyPI
    print("Uploading to PyPI...")
    run_command("python -m twine upload dist/*")

if __name__ == "__main__":
    main() 