from pydantic import BaseModel

class TasksSchema(BaseModel):
    subject : str
    tg_names : list[str]
    time_to_do : int
    tasks : list[int]
class TasksTeachersSchema(BaseModel):
    tasks : list[int]
    group_name : list[str]
    time_to_do : int