import logging
from fastapi import FastAPI
from src.middleware.error_handler import global_exception_handler
from src.middleware.session_middleware import SessionMiddleware
from src.config.config import get_settings
from src.config.cors_config import add_cors
from src.routes.api.v1 import router as v1_router
from src.utils.logger import setup_logger
from contextlib import asynccontextmanager

logger = setup_logger(__name__, level=logging.INFO)

_SETTINGS = get_settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic (before yielding)
    logger.info("Application startup...")
    yield
    # Shutdown logic (after yielding)
    logger.info("Application shutdown...")
    
app = FastAPI(
    title=_SETTINGS.service_name,
    version=_SETTINGS.k_revision,
    level=_SETTINGS.log_level,
    lifespan=lifespan,
)


add_cors(app)
app.add_middleware(SessionMiddleware)
app.add_exception_handler(Exception, global_exception_handler)

# Include the routes with versioning
app.include_router(v1_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting the application...")
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
