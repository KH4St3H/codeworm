from grammar.nscParser import nscParser


class Function:
    def __init__(self, begin_end_statement: nscParser.Begin_end_statementContext, args=()) -> None:
        self.args = args
        self.statement = begin_end_statement
