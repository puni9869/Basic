# IMPORTS
from context import Context
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter


# RUN
def run(fn, text):
    # Generate tokens
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error:
        return None, error
    print(tokens)

    # Generate AST
    parser = Parser(tokens)
    ast = parser.parse()
    if ast.error:
        return None, ast.error
    print(ast.node)

    # Run program
    interpreter = Interpreter()
    context = Context('<program>')
    result = interpreter.visit(ast.node, context)
    return result.value, result.error
