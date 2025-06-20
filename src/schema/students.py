from pydantic import BaseModel

class StudentsaddSchema(BaseModel):
    tg_id: int
    tg_name: str
class StudentsSchema(StudentsaddSchema):
    id:int
