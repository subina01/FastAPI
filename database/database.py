from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.orm import sessionmaker 

engine = create_engine("postgresql://postgres:postgres@localhost:5432/todo")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
     # Create a new database session using the `SessionLocal` instance.
    # `SessionLocal` is usually created by configuring a database engine with SQLAlchemy.
    db = SessionLocal()
    try:
         # This allows the function to act as a generator and provide the session for use in API endpoints or other operations.
        yield db
    finally:
        db.close()


def create_tables():
     # This ensures the model is loaded into the SQLModel metadata registry.
    from models.todo import Todo
    from models.users import User
    # Call `SQLModel.metadata.create_all` to create all database tables defined in the metadata.
    # `SQLModel.metadata` stores metadata about all the models that inherit from SQLModel.
    # `bind=engine` specifies the database engine to use for executing the table creation commands.
    SQLModel.metadata.create_all(bind=engine)
