from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from utils.jwt import decode_access_token
from models.users import User
from database.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )
    user_email = payload.get("sub")
    user = db.query(User).filter(User.email == user_email).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_active:  
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
