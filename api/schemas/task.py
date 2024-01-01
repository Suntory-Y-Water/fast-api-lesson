from pydantic import BaseModel, Field

class Task(BaseModel):
    id: int
    title: str | None = Field(None, example="新年からFastAPIを触る")
    done: bool = Field(False, description="タスクが完了したかどうか")