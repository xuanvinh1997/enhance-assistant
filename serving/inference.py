import json, torch
from typing import List
from logger import logger
from transformers import AutoModelForCausalLM, AutoTokenizer


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

    def perform_search(self, search_terms: List[str]) -> str:
        """
        Performs search using the model

        Args:
            search_terms (List[str]): The search terms

        Returns:
            str: The response from the model
        """
        # Create the messages
        messages = [
            {"role": "user", "content": self.tool["description"]},
            {"role": "user", "content": json.dumps(self.tool["parameter"])},
            {
                "role": "user",
                "content": f"<functioncall>{json.dumps(self.tool['name'])} "
                f"{json.dumps({'arguments': {'search_terms': search_terms}})}</functioncall>",
            },
        ]

        # Convert the messages to input ids
        input_ids = self.tokenizer.apply_chat_template(
            messages, add_generation_prompt=True, return_tensors="pt"
        ).to(self.model.device)

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
        return self.tokenizer.decode(response)

# <|assistant|> <functioncall> {"name": "search_web", "arguments": {"search_terms": ["news", "Melbourne", "May 7, 2024"]}}<|end|>

