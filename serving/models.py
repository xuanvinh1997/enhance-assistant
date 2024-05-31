from pydantic import BaseModel
from typing import List, Optional
from enum import Enum
class Role(str, Enum):
    user = "user"
    assistant = "assistant"

class Message(BaseModel):
    # enum: user, assistant
    role: str
    content: str
class InputRequest(BaseModel):
    messages: List[Message]