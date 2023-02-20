from fastapi import APIRouter
from .login import login_router
from .users import users_router
from .manga import manga_router
from .video import video_router
from .question import router as question_router
from .answer import router as answer_router
from .realestate import router as realestate_router

router = APIRouter()

router.include_router(login_router.router, prefix="/api/login", tags=["login"])
router.include_router(users_router.router, prefix="/api/users", tags=["users"])
router.include_router(manga_router.router, prefix="/api/manga", tags=["manga"])
router.include_router(video_router.router, prefix="/api/video", tags=["video"])
router.include_router(question_router.router, prefix="/api/question", tags=["question"])
router.include_router(answer_router.router, prefix="/api/answer", tags=["answer"])
router.include_router(realestate_router.router, prefix="/api/realestate", tags=["realestate"])