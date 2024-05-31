from functions.definitions import tools
from functions import execution
import json

class FunctionCalling:
    """
    Class for calling functions dynamically based on the function name.

    Attributes:
        __tools (list): List of tools with their details.

    """

    def __init__(self):
        """ Initialize the FunctionCalling class."""
        self.__tools = tools

    def __call__(self, function_name: str, function_args: str, *args, **kwargs):
        """
        Call the function based on the function name.

        Args:
            function_name (str): The name of the function to be called.
            function_args (str): The arguments to be passed to the function.

        Returns:
            The result of the called function.

        Raises:
            ValueError: If the function name is not provided or if the function is not found.

        """

        # Check if function name is provided
        if not function_name:
            raise ValueError("Function name not provided")

        # Find the function in the tools
        tool = next((tool for tool in self.__tools if tool["name"] == function_name), None)

        # Raise error if function is not found
        if not tool:
            raise ValueError(f"Function {function_name} not found")

        # Parse the function arguments
        try:
            function_args = json.loads(function_args)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error parsing function arguments: {e}")

        # Call the function
        return getattr(execution, function_name)(function_args)

