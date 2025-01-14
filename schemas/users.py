from pydantic import BaseModel, EmailStr

class Register(BaseModel):
  name: str
  email:str = EmailStr
  password: str
 
class Login(BaseModel):
  email:str = EmailStr
  password: str

class Config:
  orm_mode = True #Tells Pydantic to treat the sqlalchemy model as a dict