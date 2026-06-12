#!/usr/bin/env python3
"""Check Python version, installed packages, and directory structure."""

from __future__ import annotations

import importlib
import sys
from pathlib import Path

REQUIRED_PACKAGES = ["numpy", "pandas", "scipy", "matplotlib"]
REQUIRED_DIRS = [
    "data/raw", "data/external", "data/processed", "data/derived",
    "outputs/figures", "outputs/tables", "outputs/logs",
]


def main():
    ok = True
    print(f"Python: {sys.version}")
    print()

    print("Packages:")
    for pkg in REQUIRED_PACKAGES:
        try:
            mod = importlib.import_module(pkg)
            ver = getattr(mod, "__version__", "unknown")
            print(f"  {pkg} == {ver}")
        except ImportError:
            print(f"  {pkg} -- MISSING")
            ok = False

    print()
    print("Directories:")
    for d in REQUIRED_DIRS:
        p = Path(d)
        status = "OK" if p.is_dir() else "MISSING"
        if status == "MISSING":
            ok = False
        print(f"  {d}/  {status}")

    print()
    if ok:
        print("Environment check PASSED")
    else:
        print("Environment check FAILED -- see above")
        sys.exit(1)


if __name__ == "__main__":
    main()
