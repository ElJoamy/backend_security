from datetime import datetime, timedelta
from jose import jwt, JWTError
from src.config.config import get_settings
from src.utils.logger import setup_logger

_SETTINGS = get_settings()
logger = setup_logger(__name__, level=_SETTINGS.log_level)

def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    """
    Crea un JWT con los datos y expiración definida
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=_SETTINGS.jwt_expiration_minutes))
    to_encode.update({"exp": expire})
    
    try:
        encoded_jwt = jwt.encode(to_encode, _SETTINGS.jwt_secret, algorithm=_SETTINGS.jwt_algorithm)
        logger.debug("✅ JWT generado correctamente")
        return encoded_jwt
    except Exception as e:
        logger.error(f"❌ Error generando JWT: {e}")
        raise

def decode_access_token(token: str) -> dict | None:
    """
    Decodifica y verifica un JWT. Si es válido, devuelve su payload. Si no, devuelve None.
    """
    try:
        payload = jwt.decode(token, _SETTINGS.jwt_secret, algorithms=[_SETTINGS.jwt_algorithm])
        logger.debug("🔓 JWT decodificado exitosamente")
        return payload
    except JWTError as e:
        logger.warning(f"⚠️ Token inválido o expirado: {e}")
        return None
