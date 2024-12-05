from tokenizer import tokenize
from parser import parser
from interpreter import interpreter

def main():
    with open("test.mylang", "r") as file:
        text = file.read()
    tokens = tokenize(text)
    ast = parser(tokens)
    interpreter(ast)

main()