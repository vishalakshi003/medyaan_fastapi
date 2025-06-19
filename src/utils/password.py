from fastapi import Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import timedelta,timezone,datetime
import jwt
from strawberry import Info
from config.database import Config
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
password_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
security=HTTPBearer()


def generate_access_token(data:dict,expiry_time:timedelta=timedelta(days=1))->str:
    token = jwt.encode(payload={
        **data,
        'exp':datetime.now(timezone.utc) +expiry_time
    },algorithm=Config.JWT_ALGORITHM,key=Config.JWT_SECRET)
    return token

def jwt_decode_payload(token: str) -> dict:
    return jwt.decode(token, Config.JWT_SECRET, algorithms=Config.JWT_ALGORITHM)

def current_user(crendiatial:HTTPAuthorizationCredentials=Depends(security))->dict:
    token=crendiatial.credentials
    payload=jwt_decode_payload(token)
    return payload

