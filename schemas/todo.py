from pydantic import BaseModel, Field
from datetime import datetime

class TodoCreate(BaseModel):
  task_assigned_to: str
  task_description: str
  start_date: datetime
  due_date: datetime
  task_status: str

class Todo(BaseModel):
  id:int = Field(default=None, primary_key=True)
  task_assigned_to:str
  task_description: str
  start_date: datetime
  due_date: datetime
  task_status: str

class Config:
  orm_mode = True #Tells Pydantic to treat the sqlalchemy model as a dict