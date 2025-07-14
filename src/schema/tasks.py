from pydantic import BaseModel

class TasksSchema(BaseModel):
    subject : str
    tg_names : list[str]
    time_to_do : int
    tasks : list[int]
class TasksTeachersSchema(BaseModel):
    subject : str
    group_id : int
    time_to_do : int
    tasks : list[int]