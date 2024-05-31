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
        "name": "get_sensor_temperature",
        "description": "Retrieve the current temperature from a specific sensor",
        "parameters": {
            "type": "object",
            "properties": {
                "sensor_id": {
                    "type": "string",
                    "description": "The unique identifier of the sensor",
                },
                "sensor_type": {
                    "type": "string",
                    "description": "The type of sensor (e.g., DHT11, DS18B20)",
                },
            },
        },
    },
    {
        "name": "get_current_weather",
        "description": "Retrieve the current weather conditions for a specific location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and country or zip code of the location",
                }
            },
        },
    },
    {
        "name": "generate_release_notes",
        "description": "Generate release notes for a project based on provided information",
        "parameters": {
            "type": "object",
            "properties": {
                "project_name": {
                    "type": "string",
                    "description": "The name of the project",
                },
                "version": {
                    "type": "string",
                    "description": "The version of the release",
                },
            },
        },
    },
]
