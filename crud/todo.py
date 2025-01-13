from sqlalchemy.orm import Session
from models.todo import Todo
from schemas.todo import TodoCreate


#For creating a task
def create_task(db: Session, task:TodoCreate):
  add_task_to_db = Todo(
    task_assigned_to= task.task_assigned_to,
    task_description=task.task_description,
    start_date=task.start_date,
    due_date=task.due_date,
    task_status=task.task_status
  )
  db.add(add_task_to_db)
  db.commit()
  db.refresh(add_task_to_db)
  return add_task_to_db

# To get all tasks
def get_all_task(db: Session):
  return db.query(Todo).all()

# To get task by Id
def get_task_by_id(db: Session, task_id: int):
  return db.query(Todo).filter(Todo.id == task_id).first()

# To update the task
def update_task(db: Session, task_id: int, task:TodoCreate):
  update_task_in_db = db.query(Todo).filter(Todo.id ==task_id).first()
  if update_task_in_db:
    update_task_in_db.task_assigned_to = task.task_assigned_to
    update_task_in_db.task_description = task.task_description
    update_task_in_db.start_date = task.start_date
    update_task_in_db.due_date = task.due_date
    update_task_in_db.task_status = task.task_status
    db.commit()
    db.refresh(update_task_in_db)
    return update_task_in_db
  
# To delete the task
def delete_task(db: Session, task_id: int):
  task_to_delete = db.query(Todo).filter(Todo.id == task_id).first()
  if task_to_delete:
    db.delete(task_to_delete) 
    db.commit()
    return "Your task is deleted"
  

