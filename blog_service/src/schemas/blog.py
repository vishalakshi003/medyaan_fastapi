from pydantic import BaseModel
from typing import Optional

class Blog(BaseModel):
    title : str
    created_by : Optional[int]=None
    modified_by :Optional[int]=None
    userid : int
    
class BlogCreate(Blog):
    pass

class BlogResponse(Blog):
    id:int


    
