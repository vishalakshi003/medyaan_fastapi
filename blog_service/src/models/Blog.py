from sqlalchemy import Column,String,Integer,CHAR,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.core.config import Base

class Blog(Base):
    __tablename__ = "blog"
    id = Column(Integer,primary_key=True)
    title = Column(CHAR(20),nullable=False)
    created_by = Column(Integer,nullable=True)
    modified_by = Column(Integer,nullable=True)
    created_at = Column(DateTime,server_default=func.now(),nullable=False)
    modified_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    userid = Column(Integer,ForeignKey("custom_user.id"))
    
    user = relationship("BlogCustomUser",back_populates="bloguser")
    like = relationship("Likes",back_populates="blog")
    

class Likes(Base):
    __tablename__ = "likes"
    id = Column(Integer,primary_key=True)
    userid = Column(Integer,ForeignKey("custom_user.id"))
    blogid = Column(Integer,ForeignKey("blog.id"))
    
    user = relationship("BlogCustomUser",back_populates="bloguser")
    blog = relationship("Blog",back_populates="like")
    
    