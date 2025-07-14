from pydantic import BaseModel

class studentsaddSchema(BaseModel):
    tg_id: int = None
    tg_name: str = None
class studentsSchema(studentsaddSchema):
    id:int
