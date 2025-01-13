from fastapi import FastAPI, Depends,HTTPException
from sqlalchemy.orm import Session
from database.database import create_tables, get_db
from models.todo import Todo
from schemas.todo import TodoCreate, Todo,TodoUpdate,TodoDelete
from crud.todo import create_task, get_task_by_id, get_all_task, delete_task, update_task
app = FastAPI()


create_tables()


# Create a Task
@app.post("/todos/", response_model=Todo, tags=["Todo"])
async def task_create(todo: TodoCreate, db: Session = Depends(get_db)):
    return create_task(db= db, task = todo)

#Get all Tasks
@app.get("/todos/", response_model = list[Todo], tags=["Todo"])
async def all_task(db: Session = Depends(get_db)):
    all_task_from_db = get_all_task(db=db)
    return all_task_from_db

#Get Task By Id
@app.get("/todo/{todo_id}", response_model=Todo, tags=["Todo"])
async def task_by_id_(task_id:int, db: Session = Depends(get_db)):
    task_by_id = get_task_by_id(db=db, task_id=task_id)
    if task_by_id is None:
        raise HTTPException( status_code = 404, detail= "Task not found")
    return task_by_id

#Update a task 
@app.put("/todo/{todo_id}", response_model=Todo, tags=["Todo"])
async def task_update(task_id:int, task:TodoUpdate, db: Session = Depends(get_db)):
    task_to_update = update_task(db=db, task_id=task_id, task=task)
    if task_to_update is None:
     raise HTTPException(status_code=404, detail="Task not found")
    return task_to_update

# Delete Task
@app.delete("/todo/{todo_id}", tags=["Todo"])
async def task_delete(task_id: int, db: Session = Depends(get_db)):
    task_for_delete = delete_task(db=db, task_id=task_id)
    if task_for_delete is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task_for_delete