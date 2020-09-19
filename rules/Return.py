# from program import Parser

class Return:
    """ Defines the rules for returning values as strings, integers, and variables. """

    def __init__(self):
        print("[INTERNAL] {} class successfully loaded.".format(__name__))
        # pass

    def _print(self): # Defines printing out str/int/var
        print("[RETURN] Got response for [_print()] call from [LEXER]".format(__name__.upper()))
        # pass

    def _return(self): # Defines returning a value (like _print())
        print("[{}] Got response for [_return()] call from [LEXER]".format(__name__.upper()))
        # pass

# ret = Return()
