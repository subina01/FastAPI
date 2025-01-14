from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from utils.jwt import decode_access_token

class jwtBearer(HTTPBearer):
  def _init_(self, auto_error :bool =True):
    super(jwtBearer, self)._init_(auto_error)

  async def _call_(self, request :Request):
    credentials :HTTPAuthorizationCredentials =await super(jwtBearer, self).__call__(request)
    if credentials:
        if not credentials.scheme == "Bearer":
           raise HTTPException(status_code=403, details="Invalid")
        return credentials.credentials
    else:
       raise HTTPException(status_code= 403, details="Invalid or Expired Token!")
  
  def verify_jwt(self, jwttoken :str):
     isTokenValid : bool = False
     payload = decode_access_token(jwttoken)
     if payload:
        isTokenValid =True
        return isTokenValid