from . import login
from . import register
from . import profile
from. import logout
from fastapi import APIRouter
import sys
import os

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../")))

router = APIRouter()
router.include_router(register.router, tags=["Auth"])
router.include_router(login.router, tags=["Auth"])
router.include_router(logout.router, tags=["Auth"])
router.include_router(profile.router, tags=["User"])

