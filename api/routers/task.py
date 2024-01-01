from fastapi import APIRouter
import api.schemas.task as task_schema

router = APIRouter()

# 後々データベース接続用のtask_modelを作成するのでスキーマ定義用のtaskを区別する。

@router.get("/tasks", response_model=list[task_schema.Task])
async def list_tasks():
    return [task_schema.Task(id=1, title="first Todo task!")]


@router.post("/tasks")
async def create_task():
    pass


@router.put("/tasks/{task_id}")
async def update_task():
    pass


@router.delete("/tasks/{task_id}")
async def delete_task():
    pass