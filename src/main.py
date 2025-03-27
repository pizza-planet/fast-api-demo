from fastapi import FastAPI
from models.todo import Todo
from db import session

app = FastAPI()


@app.get("/")
def home():
    return {"message": "First FastAPI app"}


@app.post("/create")
async def create_todo(text: str, is_complete: bool = False):
    todo = Todo(text=text, is_done=is_complete)
    session.add(todo)
    session.commit()
    return {"todo added": todo.text}


@app.get("/done")
async def list_done_todos():
    todos_query = session.query(Todo)
    done_todos_query = todos_query.filter(Todo.is_done == True)
    return done_todos_query.all()


@app.get("/not_done")
async def list_not_done_todos():
    todos_query = session.query(Todo)
    not_done_todos_query = todos_query.filter(Todo.is_done == False)
    return not_done_todos_query.all()


@app.put("/update/{id}")
async def update_todo(id: int, new_text: str = "", is_complete: bool = False):
    todo_query = session.query(Todo).filter(Todo.id == id)
    todo = todo_query.first()
    if new_text:
        todo.text = new_text
    todo.is_done = is_complete
    session.add(todo)
    session.commit()
    updated_todo = todo_query.first()
    return {"todo_updated": updated_todo}


@app.delete("/delete/{id}")
async def delete_todo(id: int):
    todo = session.query(Todo).filter(Todo.id == id).first()  # Todo object
    session.delete(todo)
    session.commit()
    return {"todo deleted": todo.text}
