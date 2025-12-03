import sys
from .exceptions import exceptions

class argflow():
    def __init__(self):
        self.commands = {"--help": self._help}
        self.alias = {"-h": self._help}
        self.helper = {}

    def new_argument(self, *, flag: str, alias: str | None = None, helper: str , example: str):
        def wrapper(func):
            self.commands[flag] = func
            if alias:
                self.alias[alias] = func

            self.helper[flag] = {
                "description": helper, 
                "example": example,
                "alias": alias
            }

            return func
        return wrapper
    
    def _help(self, option=None):
        if option and option in self.commands:
            name = option
            option = self.helper[option]

            print(f"help manual for {name}{f" ({option["alias"]})" if option["alias"] is not None else ""}, provided by developer\n")
            print(option["description"]+"\n")
            print(option["example"])

            return
        
        print("help manual for program... provided by developer\n")
        for name, data in self.helper.items():
            print(f"{name}{f" ({data["alias"]})" if data["alias"] is not None else ""}: {data["description"]} | {data["example"]}")


    def parse(self, args: dict = sys.argv[1:]):
        for arg in args:
            arg = arg.split("=")

            name = arg[0]
            pairs = arg[1:]

            if pairs: pairs = arg[1].split(",")

            if name.startswith("--"): 
                if name in self.commands:
                    self.commands[name](*pairs)
                else: raise exceptions.NoArgumentFound(f"Unknown argument: {arg}"); break
            elif name.startswith("-"):
                if name in self.alias:
                    self.alias[name](*pairs)
                else: raise exceptions.NoArgumentFound(f"Unknown alias: {arg}"); break
            else: raise exceptions.NoArgumentFound(f"Unknown option: {arg}"); break