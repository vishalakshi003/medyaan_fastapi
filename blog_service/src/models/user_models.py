from src.core.config import Base
from sqlalchemy import JSON, Column,String,Integer,DateTime,Boolean,UniqueConstraint,ForeignKey
from sqlalchemy.sql import func#it will use to indicate current time 
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship


class BlogCustomUser(Base):
    __tablename__="custom_user"
    id=Column(Integer,primary_key=True)
    user_name=Column(String,nullable=False)
    email=Column(String,unique=True,nullable=False)
    mobile_number=Column(String(32),nullable=False,unique=True,index=True)
    password=Column(String,nullable=True) 
    id_proof = Column(ARRAY(JSON), default=list, nullable=False)
    created_at = Column(DateTime,server_default=func.now(),nullable=False)
    modified_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    modified_by=Column(String,nullable=True)
    is_active=Column(Boolean,default=True)
    __table_args__=(UniqueConstraint("email","mobile_number",name="unique_users")),
    
    rolemapping=relationship("BlogRoleMapping",back_populates="users")
    bloguser = relationship("Blog",back_populates="user")
    likeuser = relationship("Likes",back_populates="user")



class BlogRoleMaster(Base):
    __tablename__="role_master"
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False,unique=True)
    desc=Column(String,nullable=True)
    created_at=Column(DateTime,server_default=func.now(),nullable=False)
    modified_at=Column(DateTime,server_default=func.now(),onupdate=func.now(),nullable=False)
    is_active=Column(Boolean,default=True)   
    rolemapping=relationship("BlogRoleMapping",back_populates="roles")



class BlogRoleMapping(Base):
    __tablename__="role_mapping"
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey("custom_user.id"))
    role_id=Column(Integer,ForeignKey("role_master.id"))

    users=relationship("BlogCustomUser",back_populates="rolemapping")
    roles=relationship("BlogRoleMaster",back_populates="rolemapping")