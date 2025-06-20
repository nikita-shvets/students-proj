from pydantic import BaseModel

class groupsaddSchema(BaseModel):
    tg_id: int
    tg_name: str
class groupsSchema(groupsaddSchema):
    id:int
