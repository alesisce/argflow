"""
Exceptions for argflow.
"""

class exceptions:
    """
    Exceptions class.
    This is where you can personalise your CLI thanks to the exceptions.
    """

    class MultipleNotAllowed(Exception):
        """
        Errors when argument has been already executed and allow_multiple is false.
        """
        def __init__(self, *args):
            super().__init__(*args)

    class CantOverrideArgument(Exception):
        """
        Only present when trying to override an argument callback.
        """
        def __init__(self, *args):
            super().__init__(*args)

    class InvalidArgumentName(Exception):
        """
        Triggered when the argument can't have some characters
        """
        def __init__(self, *args):
            super().__init__(*args)

    class NoArgumentFound(Exception):
        """
        Exception only triggered when the argument you specified is not found.
        """
        def __init__(self, *args):
            super().__init__(*args)
