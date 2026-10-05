import os
from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, create_engine

DATABASE_URL = "postgresql+psycopg://app:secret@localhost:5432/appdb"

# SQLite mặc định chỉ cho 1 thread dùng connection; FastAPI dùng nhiều thread
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, echo=True, connect_args=connect_args)


def get_session():
    with Session(engine) as session:   # mỗi request 1 session, tự đóng khi xong
        yield session


SessionDep = Annotated[Session, Depends(get_session)]