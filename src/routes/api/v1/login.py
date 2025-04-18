from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.ext.asyncio import AsyncSession
from src.config.db_config import get_db
from src.services.login_service import LoginService
from src.schema.requests.login_request import LoginRequest
from src.schema.responses.token_response import TokenResponse
from src.utils.logger import setup_logger
from src.config.config import get_settings
from fastapi import APIRouter, Security
from fastapi.security import OAuth2PasswordBearer

_SETTINGS = get_settings()
logger = setup_logger(__name__, level=_SETTINGS.log_level)

router = APIRouter()
login_service = LoginService()

@router.post(
    "/login",
    response_model=TokenResponse,
    status_code=status.HTTP_200_OK,
    description="Authenticate user and return a JWT access token"
)
async def login_user(
    request: LoginRequest,
    response: Response,
    db: AsyncSession = Depends(get_db)
):
    logger.debug(f"🛎️ Received login request for {request.email}")

    token_data = await login_service.login_user(db, request)

    # Guardar el token como cookie HttpOnly (opcional)
    response.set_cookie(
        key="access_token",
        value=token_data.access_token,
        httponly=True,
        secure=False,  # True en producción con HTTPS
        samesite="lax",
        max_age=60 * 60 * 24  # 1 día
    )

    return token_data
