from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os
load_dotenv()

class Config:
    DATABASE_URL=os.getenv("DATABASEURL")
    JWT_ALGORITHM=os.getenv("JWT_ALGORITHM")
    JWT_SECRET=os.getenv("JWT_SECRET")
    
Base=declarative_base()