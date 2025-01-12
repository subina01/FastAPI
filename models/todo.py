from pydantic import BaseModel
from datetime import datetime

class TodoCreate(BaseModel):
  task_assigned_to: str
  task_description: str
  start_date: datetime
  due_date: datetime
  task_status: str
  
class Todo(BaseModel):
  id:int
  task_assigned_to:str
  task_description: str
  start_date: datetime
  due_date: datetime
  task_status: str
