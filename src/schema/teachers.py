from pydantic import BaseModel

class teachersaddSchema(BaseModel):
    name: str
    subject: str
class teacherSchema(teachersaddSchema):
    id:int
