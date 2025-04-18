from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models.user_model import User
from src.schema.requests.login_request import LoginRequest
from src.schema.responses.token_response import TokenResponse
from src.utils.password_handler import verify_password
from src.security.jwt_handler import create_access_token  # ✅ actualizado
from src.utils.logger import setup_logger
from src.config.config import get_settings

_SETTINGS = get_settings()
logger = setup_logger(__name__, level=_SETTINGS.log_level)

class LoginService:
    async def login_user(self, db: AsyncSession, credentials: LoginRequest) -> TokenResponse:
        logger.info(f"🔐 Login attempt for email: {credentials.email}")

        result = await db.execute(select(User).where(User.email == credentials.email))
        user = result.scalar_one_or_none()

        if not user:
            logger.warning(f"❌ Login failed - user not found: {credentials.email}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )

        if not verify_password(credentials.password, user.password):
            logger.warning(f"❌ Login failed - incorrect password for: {credentials.email}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )

        token = create_access_token(data={"sub": str(user.id)})
        logger.info(f"✅ Login successful for user ID {user.id} ({user.email})")

        return TokenResponse(access_token=token)
