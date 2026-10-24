from fastapi import FastAPI, Body, Path
from typing import Annotated
from models.task import Task


app = FastAPI()


@app.post("/projects/{project_id}/task/")
async def create_task(
    project_id: Annotated[int, Path(ge=1)], task: Annotated[Task, Body(embed=True)],
    created_by: str,
    priority_level: Annotated[int, Body(ge=1)] = 1,
    notify: bool = False, include_metadata: bool = True,
):
    
    data = {
        "project_id": project_id,
        "task": task,
        "created_by": created_by,
        "notify": notify,
        "include_metadata": include_metadata,
        "priority_level": priority_level,
    }
    
    if include_metadata:
        data['metada'] = {'title_lenght: ': len(task.title)}
     
    return data