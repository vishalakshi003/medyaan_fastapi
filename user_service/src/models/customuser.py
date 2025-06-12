from datetime import datetime
from sqlalchemy import ARRAY, Column, Date, DateTime,Integer,String,Float,Boolean,Text,JSON
from ..core.database import Base
from sqlalchemy.orm import relationship
class CustomUser(Base):
    __tablename__ = "users"

    id=Column(Integer,primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    balance = Column(Float)
    is_active = Column(Boolean, default=True)
    bio = Column(Text)
    preferences = Column(JSON)
    tags = Column(ARRAY(String))
    birth_date = Column(Date, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_admin=Column(Boolean,default=False)
    is_archived=Column(Boolean,default=False)
    
    users = relationship("RoleMapping",back_populates="role")