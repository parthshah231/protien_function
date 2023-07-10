from pathlib import Path


def ensure_dir(path: Path) -> Path:
    if not path.exists():
        raise FileNotFoundError(f"Directory {path} does not exist.")
    return path


ROOT = Path(__file__).resolve().parent
DATA_DIR = ensure_dir(ROOT / "data")
TRAIN_DIR = ensure_dir(DATA_DIR / "Train")
TEST_DIR = ensure_dir(DATA_DIR / "Test (Targets)")
