class Feeder:
    """ Opens the file called to get code lines. """

    def __init__(self, name):
        self.code = open(name + ".dim", "r").read()
        self.code_ln = self.code.split("\n")
        self.name = name

        print("[INTERNAL] {} class successfully loaded.".format(__name__))

    def read(self): # Returns back the contents of the file
        print("[{}] Contents for file {}.dim being read.".format(__name__.upper(), self.name))

        print("[{}] File code:".format(__name__.upper()))
        print("".join("=" for _n in range(50)))
        print(self.code)
        print("".join("=" for _n in range(50)))

        print("[{}] {} closed.".format(__name__.upper(), __name__))

        # pass

# fileopen = GetFile(None)
