from fastapi import Request, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.config.db_config import get_db
from src.models.user_model import User
from src.security.jwt_handler import decode_access_token
from src.utils.logger import setup_logger
from src.config.config import get_settings

_SETTINGS = get_settings()
logger = setup_logger(__name__, level=_SETTINGS.log_level)

async def get_current_user(
    request: Request,
    db: AsyncSession = Depends(get_db),
):
    # Buscar token en cookie o header
    token = request.cookies.get("access_token") or request.headers.get("Authorization")
    
    if token and token.startswith("Bearer "):
        token = token.split(" ")[1]

    if not token:
        logger.warning("❌ No token found in cookie or Authorization header")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")

    payload = decode_access_token(token)
    if not payload:
        logger.warning("❌ Invalid or expired token")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    user_id = payload.get("sub")
    if not user_id or not str(user_id).isdigit():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload")

    result = await db.execute(select(User).where(User.id == int(user_id)))
    user = result.scalar_one_or_none()
    if user is None:
        logger.warning(f"❌ User with ID {user_id} not found")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    return user
