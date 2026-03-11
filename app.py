from fastapi import FastAPI
from database import conn, cursor
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/app")
def frontend():
    return FileResponse("frontend/index.html")

@app.get("/")
def home():
    return {"mensagem": "API de tarefas"}

@app.post("/tarefas")
def criar_tarefas(titulo: str):
    cursor.execute(
        "INSERT INTO tarefas (titulo, concluida) VALUES (?, ?)",
        (titulo, 0)
    )

    conn.commit()

    return {"mensagem": "Tarefa criada"}


@app.get("/tarefas")
def listar_tarefas():

    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()

    return tarefas

@app.put("/tarefas/{id}")
def concluir_tarefa(id: int):

    cursor.execute(
        "UPDATE tarefas SET concluida = 1 WHERE id = ?",
        (id,)
    )

    conn.commit()
    return {"mensagem": "Tarefa concluída"}


@app.delete("/tarefas/{id}")
def deletar_tarefa(id: int):
    cursor.execute(
        "DELETE FROM tarefas WHERE id = ?",
        (id,)
    )

    conn.commit()
    return {"mensagem": "Tarefa removida"}
