# name=config.py
import os
import re
import logging
from pathlib import Path
from typing import Final

logger = logging.getLogger(__name__)

class Config:
    # Core Agent Identity & Workspace Mapping
    _RAW_VANE_ROOT_ID = os.getenv("VANE_ROOT_ID", "VANE_ROOT_ID_8A9B3C4D5E6F7G8H")
    # Sanitize the VANE_ROOT_ID to prevent path traversal / unsafe characters
    VANE_ROOT_ID: Final[str] = re.sub(r"[^A-Za-z0-9._-]", "_", _RAW_VANE_ROOT_ID)

    BASE_DIR: Final[Path] = Path(__file__).resolve().parent

    # NOTE: we DON'T create the directory at import time. Call ensure_workspace() when you actually need it.
    WORKSPACE_DIR: Final[Path] = BASE_DIR / "workspaces" / VANE_ROOT_ID

    # Vector Database Configuration
    CHROMA_PERSIST_DIR: Final[str] = str(WORKSPACE_DIR / "chroma_db")
    EMBEDDING_MODEL: Final[str] = "text-embedding-3-small"

    # LLM Orchestration
    LLM_MODEL: Final[str] = os.getenv("LLM_MODEL", "gpt-3.5-turbo")
    TEMPERATURE: Final[float] = float(os.getenv("TEMPERATURE", 0.0))
    MAX_TOKENS: Final[int] = int(os.getenv("MAX_TOKENS", 800))

    # API Network Thresholds
    API_TIMEOUT: Final[float] = float(os.getenv("API_TIMEOUT", 3.5))
    MAX_SEARCH_RESULTS: Final[int] = int(os.getenv("MAX_SEARCH_RESULTS", 4))

    # Confidence Score Boundaries
    CONFIDENCE_HIGH_THRESHOLD: Final[float] = float(os.getenv("CONFIDENCE_HIGH_THRESHOLD", 0.85))
    CONFIDENCE_MEDIUM_THRESHOLD: Final[float] = float(os.getenv("CONFIDENCE_MEDIUM_THRESHOLD", 0.60))

    @classmethod
    def validate(cls) -> None:
        """Validate numeric configuration ranges and invariants. Raises ValueError on problems."""
        if not (0.0 <= cls.CONFIDENCE_MEDIUM_THRESHOLD < cls.CONFIDENCE_HIGH_THRESHOLD <= 1.0):
            raise ValueError(
                "Confidence thresholds must satisfy: 0.0 <= medium < high <= 1.0 "
                f"(medium={cls.CONFIDENCE_MEDIUM_THRESHOLD}, high={cls.CONFIDENCE_HIGH_THRESHOLD})"
            )

        if cls.TEMPERATURE < 0.0 or cls.TEMPERATURE > 2.0:
            logger.warning("TEMPERATURE is outside typical bounds [0.0, 2.0]. Check intent.")

        if cls.API_TIMEOUT <= 0:
            raise ValueError("API_TIMEOUT must be positive")

        if cls.MAX_TOKENS <= 0:
            raise ValueError("MAX_TOKENS must be positive")

    @classmethod
    def ensure_workspace(cls, exist_ok: bool = True) -> Path:
        """
        Create the workspace directories (safe to call from CI/test setup).
        Returns the workspace path.
        """
        try:
            cls.WORKSPACE_DIR.mkdir(parents=True, exist_ok=exist_ok)
            (cls.WORKSPACE_DIR / "chroma_db").mkdir(parents=True, exist_ok=exist_ok)
        except PermissionError as e:
            # Log and re-raise so callers can decide how to handle in read-only environments
            logger.error("Failed to create workspace directory: %s (WORKSPACE_DIR=%s)", e, cls.WORKSPACE_DIR)
            raise
        return cls.WORKSPACE_DIR

# Lightweight self-check when run directly (useful for local debugging)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        Config.validate()
        ws = Config.ensure_workspace()
        logger.info("Workspace ready at %s", ws)
    except Exception as exc:
        logger.exception("Configuration validation or workspace creation failed: %s", exc)
        raise
