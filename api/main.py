import logging
from typing import Final

import uvicorn

from api.service import app

logger = logging.getLogger(__name__)


DEFAULT_ADDRESS: Final[str] = "0.0.0.0"
DEFAULT_PORT: Final[int] = 8000


def run():
    """Run the app."""
    logger.info("Starting FastAPI server...")
    uvicorn.run(app, host=DEFAULT_ADDRESS, port=DEFAULT_PORT)


if __name__ == "__main__":
    run()
