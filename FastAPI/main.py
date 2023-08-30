from fastapi import FastAPI
from model import Todo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


todos = []


# get  all todos 
@app.get("/todos")
async def get_todos():
    return {"todos": todos}


# get  single todos 
@app.get("/todos{todo_id}")
async def get_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return {'todo': todo}
    return {"massage": "NO todos Found"}


# Create todo 
@app.post("/todos")
async def create_todo(todo : Todo):
    todos.append(todo)
    return {"massage": "todos added"}


# update  todos 
@app.put("/todos{todo_id}")
async def update_todo(todo_id:int,todo_obj : Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_obj.item
            return {'todo': todo}
    return {"massage": "NO todos Found To Update"}


# delete todo
@app.get("/todos/{todo_id}")
async def delete_todos(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {'Massage': "Todo has been Deleted"}
    return {"massage": "NO todos Found"}