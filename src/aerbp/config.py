from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class ProjectConfig:
    """Configuration for the AERBP project."""
    root: Path = Path(__file__).resolve().parents[2]
    data_dir: Path = root / "data"
    raw_dir: Path = data_dir / "raw"
    processed_dir: Path = data_dir / "processed"
    reports_dir: Path = root / "reports"
    logs_dir: Path = root / "logs"
    db_path: Path = processed_dir / "aerbp.duckdb"

    start_date: str = "2018-01-01"
    end_date: str = "2026-01-01"
    initial_cash: float = 100_000.0
    transaction_cost_bps: float = 5.0  # 5 basis points
    random_seed: int = 42

CONFIG = ProjectConfig()

def ensure_project_dirs(config: ProjectConfig = CONFIG) -> None:
    """Ensure that all necessary project directories exist."""
    for directory in [config.raw_dir, config.processed_dir, config.reports_dir, config.logs_dir]:
        directory.mkdir(parents=True, exist_ok=True)

def config_summary(config: ProjectConfig = CONFIG) -> dict[str, str | float | int]:
    """Return a summary of the project configuration."""
    return {
        "root": str(config.root),
        "raw_dir": str(config.raw_dir),
        "processed_dir": str(config.processed_dir),
        "reports_dir": str(config.reports_dir),
        "logs_dir": str(config.logs_dir),
        "db_path": str(config.db_path),
        "start_date": config.start_date,
        "end_date": config.end_date,
        "initial_cash": config.initial_cash,
        "transaction_cost_bps": config.transaction_cost_bps,
        "random_seed": config.random_seed,
    }