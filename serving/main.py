from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from functions.definitions import tools
from inference import Inference
from models import InputRequest


inference = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    inference = Inference(
        model_id= "mzbac/Phi-3-mini-4k-instruct-function-calling",
        tool=tools
    )
    yield
    # Clean up the ML models and release the resources
    inference.clear()

app = FastAPI(lifespan=lifespan)

@app.get("/chat")
async def search(input: InputRequest):
    pass