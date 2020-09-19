# from program import Parser

class Comments:
    """ Defines the rules for the single and multi-line comments. """

    def __init__(self):
        # print("[INTERNAL] {} class successfully loaded.".format(__name__))
        pass

    def single_comment(self): # Defines ignoring single-line comments
        print("[{}] Got response for [single_comment()] call from [LEXER]".format(__name__.upper()))
        # pass

    def multiln_comment(self): # Defines ignoring multiple-line comments
        print("[{}] Got response for [multiln_comment()] call from [LEXER]".format(__name__.upper()))
        # pass

# com = Comments()
