from sqlalchemy import Column,Integer,String,ForeignKey
from src.core.database import Base
from sqlalchemy.orm import relationship

class RoleMaster(Base):
    __tablename__ = "rolemaster"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False)

    roles = relationship("RoleMapping",back_populates="role")
class RoleMapping(Base):
    __tablename__ = "rolemapping"
    id = Column(Integer,primary_key=True,index=True)
    userid = Column(Integer,ForeignKey("users.id"))
    roleid = Column(Integer,ForeignKey("rolemaster.id"))

    user = relationship("CustomUser",back_populates="users")
    role = relationship("RoleMaster",back_populates="roles")

