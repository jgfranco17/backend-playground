import logging
from typing import Final

import uvicorn

from app.service import app

logger = logging.getLogger(__name__)


DEFAULT_ADDRESS: Final[str] = "0.0.0.0"
DEFAULT_PORT: Final[int] = 8000


def main():
    """Run the app."""
    logger.info("Starting FastAPI server...")
    uvicorn.run(app, host=DEFAULT_ADDRESS, port=DEFAULT_PORT)
