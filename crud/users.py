from sqlalchemy.orm import Session
from models.users import User
from schemas.users import Register
from utils.jwt import get_password_hash

# To Register User
def create_user(db: Session,user:Register):
  db_user = User(
  name=user.name,
  email=user.email,
  password=get_password_hash(user.password)
  )
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  return db_user

# To Login
def get_user_by_email(db: Session, email:str):
  return db.query(User).filter(User.email == email).first()


