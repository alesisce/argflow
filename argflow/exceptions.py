"""
Exceptions for argflow.
"""

class exceptions:
    """
    Exceptions class.
    This is where you can personalise your CLI thanks to the exceptions.
    """

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
