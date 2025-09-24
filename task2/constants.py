from pathlib import Path

ENV_DIR: Path = Path(__file__).parent.resolve()
ENV_FILE: Path = ENV_DIR / ".env"