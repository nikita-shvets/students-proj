from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import async_session
from src.database import get_session

SessionDep = Annotated[async_session, Depends(get_session)]