import sys, os
import Lexer, Error

class Syntax:
    """ Defines all of the code syntax for the programming language. """

    def __init__(self):
        # works as "keyword": ["function_name", "FileName"]
        self.rules = {
            # Comments
            "#": ["single_comment", "Comments"],
            "/*/": ["multiln_comment", "Comments"],

            # Return
            "print": ["_print", "Return"],
            "return": ["_return", "Return"],

            # Statements
            "{}": ["funcparam", "Statements"],
            "if": ["_if", "Statements"],
            "while": ["_while", "Statements"],
            "for": ["_for", "Statements"],

            # Univ
            "()": ["paranthesis", "Univ"],

            # Math
            "+": ["addition", "Math"],
            "-": ["subtraction", "Math"],
            "*": ["multiplication", "Math"],
            "/": ["division", "Math"],
            "^": ["exponent", "Math"]
        }

        self.error = Error.Error()

        print("[INTERNAL] {} class successfully loaded.".format(__name__))

    def rule(self, query): # Returns back an evaluation of the rule based on keyword and file
        if query in self.rules or query == self.rules:
            exec(open("rules/{}.py".format(self.rules[query][1])).read())
            exec("class_{} = {}()\nclass_{}.{}()".format(
                self.rules[query][1].lower(),
                self.rules[query][1],
                self.rules[query][1].lower(),
                self.rules[query][0]
            ))

            print("[{}] Successfully ran [{}] class, from [{}] statement.".format(__name__.upper(), self.rules[query][1].upper(), query))
            print("[{}] Rule table closed.".format(__name__.upper()))
        else:
            self.error.i_give(1) # Give 'empty value' internal error
