from grammar.nscParser import nscParser
from .interpreter import Interpreter


class Function:
    def __init__(self, name, interpreter: Interpreter, statements: nscParser.StatementsContext, args=()) -> None:
        self.name = name
        self.args = args
        self.statements = statements
        self.interpreter = interpreter

    def call(self, values: list):
        if len(values) != len(self.args):
            raise ValueError(f'Function required {len(self.args)} arguments but {len(values)} were given')

        variables = self.interpreter.global_variables.copy()
        function_args = {key: val for key, val in zip(self.args, values)}
        functions = self.interpreter.functions.copy()

        new_interpreter = Interpreter(global_variables=variables, local_variables=function_args, functions=functions)
        new_interpreter.inside_function = True
        new_interpreter.visitStatements(self.statements)

        if new_interpreter.function_return_value is not None:
            return new_interpreter.function_return_value
