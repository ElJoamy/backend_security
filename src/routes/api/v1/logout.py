from fastapi import APIRouter, Response, status
from src.utils.logger import setup_logger
from src.config.config import get_settings

_SETTINGS = get_settings()
logger = setup_logger(__name__, level=_SETTINGS.log_level)

router = APIRouter()

@router.post(
    "/logout",
    status_code=status.HTTP_200_OK,
    summary="Logout user",
    description="Clears the access_token cookie and logs the user out."
)
async def logout_user(response: Response):
    response.delete_cookie("access_token")
    logger.info("👋 User logged out, cookie cleared")
    return {"message": "Logged out successfully."}
