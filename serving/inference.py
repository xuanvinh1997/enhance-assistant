import json, torch
from typing import List
from logger import logger
from transformers import AutoModelForCausalLM, AutoTokenizer
from models import Message


class Inference:
    """Class for performing inference using the model"""

    def __init__(self, model_id: str, tool: dict):
        """
        Initializes the Inference class

        Args:
            model_id (str): The model id to be used for inference
            tool (dict): The tool details
        """
        logger.info(f"Loading model: {model_id}")
        self.model_id = model_id
        self.tool = tool

        # Initialize the tokenizer and model
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_id, torch_dtype=torch.bfloat16, device_map="auto"
        )

        # Define the terminators
        self.terminators = [
            self.tokenizer.eos_token_id,
            self.tokenizer.convert_tokens_to_ids("<|end|>"),
        ]

    def clear(self):
        """
        Clears the model and tokenizer
        """
        self.model = None
        self.tokenizer = None
    
    def __tokenize(self, messages):
        # Convert the messages to input ids
        input_ids = self.tokenizer.apply_chat_template(
            messages, add_generation_prompt=True, return_tensors="pt"
        ).to(self.model.device)

    def get_response(self, messages: List[Message]) -> str:
        """
        Performs search using the model

        Args:
            messages (List[Message]): The messages to be used for search
        Returns:
            str: The response from the model
        """
        # Add the custom message before latest message
        messages.insert(
            -1,
            Message(
                role="user",
                content=f"You are a helpful assistant with access to the following functions. Use them if required - {str(self.tool)}",
            ),
        )
        if not isinstance(self.model, AutoModelForCausalLM):
            raise ValueError("Model is not initialized")
        
        input_ids = self.__tokenize([message.model_dump() for message in messages])
        # Generate the response
        outputs = self.model.generate(
            input_ids,
            max_new_tokens=256,
            eos_token_id=self.terminators,
            do_sample=True,
            temperature=0.1,
        )

        # Decode the response
        response = outputs[0]
        first = self.tokenizer.decode(response)
        print(first)


# <|assistant|> <functioncall> {"name": "search_web", "arguments": {"search_terms": ["news", "Melbourne", "May 7, 2024"]}}<|end|>
