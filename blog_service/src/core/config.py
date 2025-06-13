from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os
load_dotenv()

class Config:
    DATABASE_URL=os.getenv("DATABASEURL")
    
Base=declarative_base()