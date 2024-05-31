from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from functions.definitions import tools
from inference import Inference
from models import InputRequest
from adapter.file_adapter import FileAdapter
from adapter.mqtt_adapter import MQTTAdapter
from adapter.search_adapter import SearchAdapter

adapters = [FileAdapter(), SearchAdapter(), MQTTAdapter(broker="localhost", port=1883, topic="temperature", client_id="test")]
inference = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start stream from IoT

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
    # Get the chat response
    return inference.get_response(input)