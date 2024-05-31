tools = [
    {
        "name": "get_token_price",
        "description": "Get the current cryptocurrency token price",
        "parameters": {
            "type": "object",
            "properties": {
                "crypto_symbol": {
                    "type": "string",
                    "description": "The symbol of the cryptocurrency",
                    "required": True,
                }
            },
        },
    },
    {
        "name": "get_weather",
        "description": "Get the current weather",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The city to get the weather for",
                }
            },
        },
    },
]
