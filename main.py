from fastapi import FastAPI, Depends,HTTPException
from sqlalchemy.orm import Session
from database.database import create_tables, get_db
from models.todo import Todo
from models.users import User
from schemas.todo import TodoCreate, Todo,TodoUpdate,TodoDelete
from schemas.users import Register,Login
from crud.todo import create_task, get_task_by_id, get_all_task, delete_task, update_task
from crud.users import create_user,get_user_by_email
from utils.jwt import create_access_token, verify_password
from utils.jwt_auth import get_current_user
from utils.jwt_bearer import jwtBearer

app = FastAPI()


create_tables()

# Configuration for OAuth

# To store user sessions


# Login via google


# Endpoint for Callback



# Register user
@app.post("/register", response_model=Register,tags=["auth"])
async def register(user: Register, db:Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email== user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email is already registered.")
    created_user = create_user(db=db, user=user)
    return created_user

# Login
@app.post("/Login",tags=["auth"])
def login(user: Login, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db=db, email=user.email)
    if not existing_user:
        raise HTTPException(status_code=401, detail="Invalid email")
    if not verify_password(user.password, existing_user.password):
        raise HTTPException(status_code=404, detail="Invalid password")

    access_token = create_access_token(data={"sub": existing_user.email})
    return {"access_token": access_token, "token_type": "bearer"}

 # Create a Task
@app.post("/", response_model=Todo,dependencies=[Depends(jwtBearer())] ,tags=["todo"])
async def task_create(todo: TodoCreate, db: Session = Depends(get_db)):
    return create_task(db= db, task = todo)

#Get all Tasks
@app.get("/", response_model = list[Todo],dependencies=[Depends(jwtBearer())] ,tags=["todo"])
async def all_task(db: Session = Depends(get_db)):
    all_task_from_db = get_all_task(db=db)
    return all_task_from_db

#Get Task By Id
@app.get("/", response_model=Todo,dependencies=[Depends(jwtBearer())] ,tags=["todo"])
async def task_by_id_(task_id:int, db: Session = Depends(get_db)):
    task_by_id = get_task_by_id(db=db, task_id=task_id)
    if task_by_id is None:
        raise HTTPException( status_code = 404, detail= "Task not found")
    return task_by_id

#Update a task 
@app.put("/", response_model=Todo,dependencies=[Depends(jwtBearer())] ,tags=["todo"])
async def task_update(task_id:int, task:TodoUpdate, db: Session = Depends(get_db)):
    task_to_update = update_task(db=db, task_id=task_id, task=task)
    if task_to_update is None:
     raise HTTPException(status_code=404, detail="Task not found")
    return task_to_update

# Delete Task
@app.delete("/",dependencies=[Depends(jwtBearer())] ,tags=["todo"])
async def task_delete(task_id: int, db: Session = Depends(get_db)):
    task_for_delete = delete_task(db=db, task_id=task_id)
    if task_for_delete is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task_for_delete

