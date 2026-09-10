from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API de Tarefas")
tarefas = [] # "banco" em memória (só para a aula)

class Tarefa(BaseModel): # o TIPO da entrada → vira validação + /docs
    titulo: str