from sqlalchemy import Column,Integer,String
from src.core.database import Base

class RoleMaster(Base):
    __tablename__ = "rolemaster"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False)
