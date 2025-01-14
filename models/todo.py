from sqlmodel import SQLModel, Field
from datetime import datetime

class Todo(SQLModel, table=True):  
    id: int = Field(default=None, primary_key=True) 
    task_assigned_to: str
    task_description: str
    start_date: datetime = Field(default_factory=datetime.utcnow)
    due_date: datetime
    task_status: str