#!/usr/bin/env python3
"""
env_bootstrap.py
----------------
Creates a local Python virtual environment and installs dependencies.

Usage:
  python env_bootstrap.py
  python env_bootstrap.py --venv .venv --upgrade
  python env_bootstrap.py --requirements requirements.txt
"""

import argparse
import os
import platform
import subprocess
import sys
from pathlib import Path


def run(cmd, cwd=None):
    print(f"\n> {' '.join(cmd)}")
    subprocess.check_call(cmd, cwd=cwd)


def venv_python(venv_dir: Path) -> Path:
    if platform.system().lower().startswith("win"):
        return venv_dir / "Scripts" / "python.exe"
    return venv_dir / "bin" / "python"


def ensure_venv(venv_dir: Path):
    if venv_dir.exists():
        print(f"[OK] Virtual environment already exists: {venv_dir}")
        return

    print(f"[INFO] Creating virtual environment at: {venv_dir}")
    run([sys.executable, "-m", "venv", str(venv_dir)])
    print("[OK] Virtual environment created.")


def pip_install(py: Path, requirements: Path, upgrade: bool = False):
    # Always ensure pip tooling exists/updated
    run([str(py), "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"])

    if requirements.exists():
        cmd = [str(py), "-m", "pip", "install", "-r", str(requirements)]
        if upgrade:
            cmd.append("--upgrade")
        run(cmd)
        print("[OK] Dependencies installed.")
    else:
        print(f"[WARN] Requirements file not found: {requirements} (skipping install)")


def print_activation_help(venv_dir: Path):
    if platform.system().lower().startswith("win"):
        print("\nActivate the environment (Windows):")
        print(f"  {venv_dir}\\Scripts\\activate")
    else:
        print("\nActivate the environment (Linux/macOS):")
        print(f"  source {venv_dir}/bin/activate")


def main():
    parser = argparse.ArgumentParser(description="Bootstrap Python virtual environment.")
    parser.add_argument("--venv", default=".venv", help="Virtualenv folder name (default: .venv)")
    parser.add_argument("--requirements", default="requirements.txt", help="Requirements file path")
    parser.add_argument("--upgrade", action="store_true", help="Upgrade packages when installing requirements")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent
    venv_dir = repo_root / args.venv
    requirements = repo_root / args.requirements

    ensure_venv(venv_dir)
    py = venv_python(venv_dir)

    pip_install(py, requirements=requirements, upgrade=args.upgrade)
    print_activation_help(venv_dir)

    print("\nQuick test:")
    print(f"  {py} tools/lab_snapshot.py --help")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"\n[ERROR] Command failed with exit code {e.returncode}")
        sys.exit(e.returncode)
