"""Offline archive verification; model weights/network are not needed."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from verify_results import audit

if __name__ == "__main__":
    audit()
