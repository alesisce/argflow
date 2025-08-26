import sys
import inspect
from .exceptions import exceptions

class argflow:
    def __init__(self, argv: dict = None) -> None:
        self.arguments = {}
        self.argv = sys.argv[1:] if not argv else argv # Uses argv from the argv argument if avaliable.
        #print(self.argv)

    def _execute_argument(self, argument_name: str) -> None:
        if not argument_name in self.arguments:
            raise exceptions.NoArgumentFound(f"No argument '{argument_name}'.") # Raising if not existing.
        
        argument_index = self.argv.index(argument_name) # Getting index for the argument
        function_arg_index = argument_index + 1 # The index arguments for the argument (Does not make sense)

        # Getting the necessary data.
        arg_count = self.arguments[argument_name]["arg_count"]
        arg_positional = self.arguments[argument_name]["positional"]
        arg_callback = self.arguments[argument_name]["callback"]

        try: args_for_callback = self.argv[function_arg_index:] # The arguments of the callback
        except IndexError: args_for_callback = [] # defaults to empty list.

        parsed = {}
        for index in range(arg_count):
            try: value = args_for_callback[index] # Arg found
            except IndexError: break # Arg not found and exit loop

            if "--" in value and "=" in value:
                optional_arg = value.split("=", 1)
                optional_arg_name = optional_arg[0].removeprefix("--")
                optional_arg_value = optional_arg[1]

                parsed[optional_arg_name] = optional_arg_value
                continue
            elif "--" in value: break

            try: parsed[arg_positional[index]] = value
            except: break
        
        del self.argv[argument_index] # Remove the command to not confuse the parser.

        arg_callback(**parsed)

    def new_argument(self, argument_name: str, argument_callback, allow_multiple: bool = False) -> None:
        """
        Adding a new argument to the argflow parser.
        """
        if argument_name.startswith("-") or " " in argument_name:
            raise exceptions.InvalidArgumentName(f"Invalid argument name for: {argument_name}")

        if argument_name in self.arguments:
            raise exceptions.CantOverrideArgument(f"You can't override an argument ({argument_name}) if it was already specified.")

        argument_name = "--"+argument_name

        signature = inspect.signature(argument_callback)
        
        obligatory = [
            name for name, param in signature.parameters.items() # Finding positional arguments
            if param.default is inspect._empty
        ]
        optional = {
            name: param.default for name, param in signature.parameters.items() # Finding optional function arguments
            if param.default is not inspect._empty
        }

        self.arguments[argument_name] = {
            "arg_count": len(obligatory) + len(optional),
            "positional": obligatory,
            "multiple": allow_multiple,
            "callback": argument_callback
        }

    def parse(self, on_default=None, ignore_args: bool = False):
        already_parsed = [] # this will save arguments that cannot be parsed again.

        if callable(on_default) and not ignore_args and not self.argv: # Calling on_default if no arguments are supplied and no ignore_args..
            on_default()
            return

        for arg in self.argv:
            if arg.startswith("--") and not "=" in arg:
                if not arg in self.arguments:
                    raise exceptions.NoArgumentFound(f"No argument '{arg}'.") # Raising if not existing.

                if not arg in already_parsed and not self.arguments[arg]["multiple"]:
                    already_parsed.append(arg) # Adding to already_parsed

                    # Executing
                    self._execute_argument(arg)
                else:
                    raise exceptions.MultipleNotAllowed(f"Can't execute '{arg}' multiple times because allow_multiple is disabled.")
                
        if callable(on_default) and ignore_args: # Calling on_default if ignore_args is supplied..
            on_default()
            return