from antlr4 import InputStream, CommonTokenStream
from grammar.nscLexer import nscLexer
from grammar.nscParser import nscParser
from grammar.nscVisitor import nscVisitor
from .expr_visitor import NscVisitorImpl
import logging

logging.basicConfig(level=logging.DEBUG)


class Interpreter(NscVisitorImpl, nscVisitor):
    def __init__(self, global_variables={}, local_variables={}, functions={}):
        self.global_variables = global_variables
        self.variables = global_variables
        self.variables.update(local_variables)
        self.functions = functions
        self.inside_function = False
        self.has_returned = False
        self.function_return_value = None

    def visitIdentifier(self, ctx):
        if ctx.ID():
            return self.variables.get(ctx.ID().getText(), None)

    def visitProgram(self, ctx):
        return self.visitStatements(ctx.statements())

    def visitStatements(self, ctx):
        for statement in ctx.statement():
            self.visitStatement(statement)

    def visitStatement(self, ctx):
        if self.inside_function and self.has_returned:
            return

        if c := ctx.assign_statement():
            var_name = c.ID().getText()
            value = self.visitExpr(c.expr())
            self.variables[var_name] = value

        elif c := ctx.begin_end_statement():
            self.visitStatements(c.statements())

        elif c := ctx.if_else_statement():
            statements = c.statement()
            if self.visitExpr(c.expr()):
                self.visitStatement(c.statement(0))
            elif len(statements) > 1:
                self.visitStatement(c.statement(1))

        elif c := ctx.while_statement():
            while self.visitExpr(c.expr()):
                self.visitStatement(c.statement())

        elif c := ctx.for_statement():
            var_name = c.ID().getText()
            start = int(c.NUMBER(0).getText())
            end = int(c.NUMBER(1).getText())
            for i in range(start, end + 1):
                self.variables[var_name] = i
                self.visitStatement(c.statement())

        elif c := ctx.loop_statement():
            var_name = c.ID().getText()
            count = int(c.NUMBER().getText())
            for i in range(1, count + 1):
                self.variables[var_name] = i
                self.visitStatement(c.statement())

        elif c := ctx.print_simple():
            output = []
            if c.ID():
                var_name = c.ID().getText()
                if var_name in self.variables:
                    output.append(str(self.variables[var_name]))
                else:
                    output.append("undefined")
            self.print_output(" ".join(output))

        elif c := ctx.print_literal():
            output = []
            if c.STRING():
                output.append(c.STRING().getText()[1:-1])
            if c.ID():
                var_name = c.ID().getText()
                if var_name in self.variables:
                    output.append(str(self.variables[var_name]))
                else:
                    output.append("undefined")
            self.print_output(" ".join(output))

        elif c := ctx.function_declration_statement():
            self.visit(c)

        elif c := ctx.function_call_statement():
            self.visit(c)

        elif c := ctx.return_statement():
            self.visit(c)

    def visit(self, tree):
        if self.has_returned:
            return self.function_return_value
        return super().visit(tree)

    def visitFunction_declration_statement(self, ctx: nscParser.Function_declration_statementContext):
        from .function import Function
        func_name = ctx.ID().getText()
        if func_name in self.functions:
            raise NameError(f"Function with name {func_name} already declared.")

        args = []
        for argctx in ctx.function_arg():
            args.append(argctx.ID().getText())

        func = Function(func_name, self, ctx.begin_end_statement().statements(), tuple(args))
        self.functions[func_name] = func

    def visitReturn_statement(self, ctx: nscParser.Return_statementContext):
        if not self.inside_function:
            raise SyntaxError('return statement should be used inside a function')
        if self.has_returned:
            return self.function_return_value
        result = self.visit(ctx.expr())
        self.function_return_value = result
        self.has_returned = True
        return result

    def visitFunction_call_statement(self, ctx: nscParser.Function_call_statementContext):
        return self.visit(ctx.function_call())

    def visitFunction_call(self, ctx: nscParser.Function_callContext):
        func_name = ctx.ID().getText()
        function = self.functions.get(func_name)
        if not function:
            raise NameError(f'Funcion "{func_name}" does not exist')
        args = []
        for c in ctx.expr():
            args.append(self.visit(c))

        return function.call(args)

    def visitFunctionCall(self, ctx: nscParser.FunctionCallContext):
        return self.visit(ctx.function_call())

    def visitID(self, ctx):
        var_name = ctx.getText()
        if var_name in self.variables:
            return self.variables[var_name]
        raise NameError(f"Variable '{var_name}' is not defined")

    def strToNumber(self, s):
        try:
            return int(s)
        except ValueError:
            return float(s)

    def print_output(self, output):
        print(output)  # Placeholder for GUI output function

    @staticmethod
    def run_code(code):
        input_stream = InputStream(code)
        lexer = nscLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = nscParser(stream)
        tree = parser.program()

        interpreter = Interpreter()

        try:
            interpreter.visit(tree)
        except Exception as e:
            logging.error(e.with_traceback())
