from typing import Annotated
from fastapi import Depends
from redis import Redis
from sqlmodel.ext.asyncio.session import AsyncSession

from src.extensions import Extensions


class BaseService:
    def __init__(
        self,
        session: Annotated[AsyncSession, Depends(Extensions.db)],
        redis: Annotated[Redis, Depends(Extensions.redis)],
    ) -> None:
        self.session = session
        self.redis = redis
