import logging
from http import HTTPStatus

from fastapi import APIRouter, HTTPException

logger = logging.getLogger(__name__)


router_v0 = APIRouter(prefix="/v0", tags=["v0"])


@router_v0.get("/greet")
def greet(name: str | None = None) -> dict[str, str]:
    """Greet the user."""
    if not name:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Name cannot be empty",
        )
    return {"message": f"Hello, {name}!"}
