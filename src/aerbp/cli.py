from aerbp import __version__
from aerbp.config import ensure_project_dirs, config_summary
from aerbp.logging_utils import get_logger

logger = get_logger(__name__)

def main() -> None:
    ensure_project_dirs()
    logger.info("AERBP project directories are ready.")
    logger.info("AERBP version: %s", __version__)

    print("AERBP Project Configuration:")
    print("============================")
    for key, value in config_summary().items():
        print(f"{key}: {value}")    