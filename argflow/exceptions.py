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

    class NoArgumentFound(Exception):
        """
        Exception only triggered when the argument you specified is not found.
        """
        def __init__(self, *args):
            super().__init__(*args)

    class ToMuchPositionals(Exception):
        """
        Only happens when there is to much positionals to handle and functions only can handle a certain amount.
        """
        def __init__(self, *args):
            super().__init__(*args)

    class MissingPositionalArgument(Exception):
        """
        Exception triggered when arguments are not optional and are missing.
        """
        def __init__(self, *args):
            super().__init__(*args)

    class ParseFail(Exception):
        """
        Exception when the parsing fails. Rarely happens.
        """
        def __init__(self, *args):
            super().__init__(*args)