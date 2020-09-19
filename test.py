import sys, os
import Lexer, Feeder

filename = Feeder.Feeder("testing")
lex = Lexer.Lexer(filename.code)

filename.read()

needs = ["#", "///", "print", "return"]

for j in needs:
    lex.lex(j)
