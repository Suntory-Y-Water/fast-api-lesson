import datetime
from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: str | None = Field(None, json_schema_extra={"example": "新年からFastAPIを触る"})
    due_date: datetime.date | None = Field(None, json_schema_extra={"example": "2024-01-01"})


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    done: bool = Field(False, description="タスクが完了したかどうか")

    class ConfigDict:
        from_attributes = True


class TaskCreateResponse(TaskCreate):
    id: int

    class ConfigDict:
        from_attributes = True
