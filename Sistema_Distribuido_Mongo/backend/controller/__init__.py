from fastapi import APIRouter

from backend.controller import musicas_controller

router = APIRouter(prefix="/api")
router.include_router(musicas_controller.singular)
