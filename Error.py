import sys, os

class Error:
    """ Gives back error statements upon failcheck. """

    def __init__(self):
        print("[INTERNAL] {} class successfully loaded.".format(__name__))
        # pass

    def i_give(self, value): # Gives back internal error with defined value
        if value == 0:
            print("[{}] Failed to finish code statement.".format(__name__.upper()))
        elif value == 1:
            print("[{}] Missing un-recognizable value, empty.".format(__name__.upper()))
        else:
            print("[{}] Could not throw exception for error ID {}".format(__name__.upper(), value))

        sys.exit()

    def c_give(self, value): # Gives back client error with defined value (for code)
        pass
