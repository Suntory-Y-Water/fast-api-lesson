from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: str | None = Field(None, example="新年からFastAPIを触る")


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    done: bool = Field(False, description="タスクが完了したかどうか")

    class Config:
        orm_mode = True


class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True
