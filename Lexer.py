import sys, os, time
import Error, Syntax

class Lexer:
    """ A fully coded lexer able to parse the code into a list for keys. """

    def __init__(self, strip):
        self.code = strip
        self.char = list(strip) # splits by char; no whitespace
        self.keys = {
            "state": False,
            "string": False,
            "line": False,
            "whitespace": 0,
            "operator": False,
            "opertype": "",
            "tokens": []
        }

        self.error = Error.Error()
        self.syntax = Syntax.Syntax()

        print("[INTERNAL] {} class successfully loaded.".format(__name__))
        # pass

    def lex(self, key=None): # Defines key statements for their statements
        # Dependency values for lexer
        token = ""

        # Timestamp
        first_time = time.time()

        if key in [None, ""]:
            self.error.i_give(1) # Give 'value empty' internal error
        else:
            print("[{}] Began lexing process, looking for [{}].".format(__name__.upper(), key))

            for char in self.char: # Checks every char in self.ch
                token += char

                if " " in token: # If whitespace detected
                    self.keys["whitespace"] += 1
                    token = ""
                elif "\n" in token: # If newline detected
                    self.keys["line"] = True
                    token = ""
                elif "'" in token or '"' in token: # If string quotes detected
                    if self.keys["string"] == False: # If string is not started
                        self.keys["string"] = True
                    else:
                        self.keys["string"] = False

                    token = ""
                elif "+" in token or "-" in token or "/" in token or "*" in token or "^" in token: # If math operators detected
                    if self.keys["operator"] == False: # If operator was non-existant
                        self.keys["operator"] = True
                    else:
                        self.keys["operator"] = False

                    if "+" in token:
                        self.keys["opertype"] = "+"
                    elif "-" in token:
                        self.keys["opertype"] = "-"
                    elif "/" in token:
                        self.keys["opertype"] = "/"
                    elif "*" in token:
                        self.keys["opertype"] = "*"
                    elif "^" in token:
                        self.keys["opertype"] = "^"

                    token = ""
                elif token == key: # If the token is with the key
                    self.keys["state"] = True

                    print("[{}] Recognized token [{}], looked for [{}]".format(__name__.upper(), token, key))
                    print("[{}] Token registry complete, took {} seconds.".format(__name__.upper(), time.time() - first_time))

                    self.syntax.rule(token)
                    self.keys["tokens"].append(token)
                    token = ""
                else:
                    self.keys["state"] = False
                    self.keys["line"] = False

                    print("[{}] Added to token [{}]".format(__name__.upper(), token))

        print("[{}] {} closed.".format(__name__.upper(), __name__))
        return token

# lex = Lexer(None)
