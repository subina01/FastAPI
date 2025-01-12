from sqlmodel import SQLModel, create_engine, Session
from sqlmodel import Session as SQLSession

engine = create_engine("postgresql://postgresql:postgres@localhost:5432/todo")

SessionLocal = SQLSession(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    from models.todo import Todo
    from models.users import User
    SQLModel.metadata.create_all(bind=engine)
