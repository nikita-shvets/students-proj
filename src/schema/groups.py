from pydantic import BaseModel

class groupsaddSchema(BaseModel):
    teachers_id: int
    students_names: str
class groupsSchema(groupsaddSchema):
    id:int
