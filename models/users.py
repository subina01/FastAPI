from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):  
    id: int = Field(default=None, primary_key=True)  
    name: str
    email: str = Field(unique=True, index=True)
    password: str