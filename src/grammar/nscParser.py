# Generated from nsc.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,178,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,1,0,1,1,1,1,1,2,5,2,48,8,2,10,2,12,2,51,9,2,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,3,3,62,8,3,1,4,1,4,1,4,1,4,5,4,68,8,4,10,
        4,12,4,71,9,4,1,5,1,5,1,5,1,5,5,5,77,8,5,10,5,12,5,80,9,5,1,6,1,
        6,1,6,1,6,5,6,86,8,6,10,6,12,6,89,9,6,1,7,1,7,1,7,5,7,94,8,7,10,
        7,12,7,97,9,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,105,8,8,1,9,1,9,1,9,1,
        9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,
        1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,3,13,132,8,13,1,14,1,14,
        1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,5,17,
        161,8,17,10,17,12,17,164,9,17,1,17,3,17,167,8,17,1,17,1,17,1,17,
        1,18,1,18,1,19,1,19,1,20,1,20,1,20,0,0,21,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,0,3,1,0,21,26,1,0,27,29,1,0,
        30,31,174,0,42,1,0,0,0,2,44,1,0,0,0,4,49,1,0,0,0,6,61,1,0,0,0,8,
        63,1,0,0,0,10,72,1,0,0,0,12,81,1,0,0,0,14,90,1,0,0,0,16,104,1,0,
        0,0,18,106,1,0,0,0,20,111,1,0,0,0,22,115,1,0,0,0,24,119,1,0,0,0,
        26,125,1,0,0,0,28,133,1,0,0,0,30,138,1,0,0,0,32,147,1,0,0,0,34,154,
        1,0,0,0,36,171,1,0,0,0,38,173,1,0,0,0,40,175,1,0,0,0,42,43,5,32,
        0,0,43,1,1,0,0,0,44,45,3,4,2,0,45,3,1,0,0,0,46,48,3,6,3,0,47,46,
        1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,5,1,0,0,0,51,
        49,1,0,0,0,52,62,3,18,9,0,53,62,3,20,10,0,54,62,3,26,13,0,55,62,
        3,28,14,0,56,62,3,30,15,0,57,62,3,32,16,0,58,62,3,22,11,0,59,62,
        3,24,12,0,60,62,3,34,17,0,61,52,1,0,0,0,61,53,1,0,0,0,61,54,1,0,
        0,0,61,55,1,0,0,0,61,56,1,0,0,0,61,57,1,0,0,0,61,58,1,0,0,0,61,59,
        1,0,0,0,61,60,1,0,0,0,62,7,1,0,0,0,63,69,3,10,5,0,64,65,3,36,18,
        0,65,66,3,10,5,0,66,68,1,0,0,0,67,64,1,0,0,0,68,71,1,0,0,0,69,67,
        1,0,0,0,69,70,1,0,0,0,70,9,1,0,0,0,71,69,1,0,0,0,72,78,3,12,6,0,
        73,74,3,40,20,0,74,75,3,12,6,0,75,77,1,0,0,0,76,73,1,0,0,0,77,80,
        1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,11,1,0,0,0,80,78,1,0,0,0,
        81,87,3,14,7,0,82,83,3,38,19,0,83,84,3,14,7,0,84,86,1,0,0,0,85,82,
        1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,13,1,0,0,0,
        89,87,1,0,0,0,90,95,3,16,8,0,91,92,5,1,0,0,92,94,3,16,8,0,93,91,
        1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,15,1,0,0,0,
        97,95,1,0,0,0,98,99,5,2,0,0,99,100,3,8,4,0,100,101,5,3,0,0,101,105,
        1,0,0,0,102,105,5,32,0,0,103,105,5,33,0,0,104,98,1,0,0,0,104,102,
        1,0,0,0,104,103,1,0,0,0,105,17,1,0,0,0,106,107,5,32,0,0,107,108,
        5,4,0,0,108,109,3,8,4,0,109,110,5,5,0,0,110,19,1,0,0,0,111,112,5,
        6,0,0,112,113,3,4,2,0,113,114,5,7,0,0,114,21,1,0,0,0,115,116,5,8,
        0,0,116,117,5,32,0,0,117,118,5,5,0,0,118,23,1,0,0,0,119,120,5,8,
        0,0,120,121,5,34,0,0,121,122,5,9,0,0,122,123,5,32,0,0,123,124,5,
        5,0,0,124,25,1,0,0,0,125,126,5,10,0,0,126,127,3,8,4,0,127,128,5,
        11,0,0,128,131,3,6,3,0,129,130,5,12,0,0,130,132,3,6,3,0,131,129,
        1,0,0,0,131,132,1,0,0,0,132,27,1,0,0,0,133,134,5,13,0,0,134,135,
        3,8,4,0,135,136,5,14,0,0,136,137,3,6,3,0,137,29,1,0,0,0,138,139,
        5,15,0,0,139,140,5,32,0,0,140,141,5,16,0,0,141,142,5,33,0,0,142,
        143,5,17,0,0,143,144,5,33,0,0,144,145,5,14,0,0,145,146,3,6,3,0,146,
        31,1,0,0,0,147,148,5,18,0,0,148,149,5,32,0,0,149,150,5,19,0,0,150,
        151,5,33,0,0,151,152,5,14,0,0,152,153,3,6,3,0,153,33,1,0,0,0,154,
        155,5,20,0,0,155,156,5,32,0,0,156,166,5,2,0,0,157,158,3,0,0,0,158,
        159,5,9,0,0,159,161,1,0,0,0,160,157,1,0,0,0,161,164,1,0,0,0,162,
        160,1,0,0,0,162,163,1,0,0,0,163,165,1,0,0,0,164,162,1,0,0,0,165,
        167,3,0,0,0,166,162,1,0,0,0,166,167,1,0,0,0,167,168,1,0,0,0,168,
        169,5,3,0,0,169,170,3,20,10,0,170,35,1,0,0,0,171,172,7,0,0,0,172,
        37,1,0,0,0,173,174,7,1,0,0,174,39,1,0,0,0,175,176,7,2,0,0,176,41,
        1,0,0,0,10,49,61,69,78,87,95,104,131,162,166
    ]

class nscParser ( Parser ):

    grammarFileName = "nsc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'^'", "'('", "')'", "'='", "';'", "'begin'", 
                     "'end'", "'print'", "','", "'if'", "'then'", "'else'", 
                     "'while'", "'do'", "'for'", "'of'", "'to'", "'loop'", 
                     "':'", "'fn'", "'>'", "'<='", "'>='", "'=='", "'!='", 
                     "'<'", "'*'", "'/'", "'%'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "NUMBER", "STRING", "WS", "COMMENT" ]

    RULE_function_arg = 0
    RULE_program = 1
    RULE_statements = 2
    RULE_statement = 3
    RULE_expr = 4
    RULE_cumTerm = 5
    RULE_term = 6
    RULE_factor = 7
    RULE_exponent = 8
    RULE_assign_statement = 9
    RULE_begin_end_statement = 10
    RULE_print_simple = 11
    RULE_print_literal = 12
    RULE_if_else_statement = 13
    RULE_while_statement = 14
    RULE_for_statement = 15
    RULE_loop_statement = 16
    RULE_function_declration = 17
    RULE_cumopr = 18
    RULE_multiplicative = 19
    RULE_additive = 20

    ruleNames =  [ "function_arg", "program", "statements", "statement", 
                   "expr", "cumTerm", "term", "factor", "exponent", "assign_statement", 
                   "begin_end_statement", "print_simple", "print_literal", 
                   "if_else_statement", "while_statement", "for_statement", 
                   "loop_statement", "function_declration", "cumopr", "multiplicative", 
                   "additive" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    ID=32
    NUMBER=33
    STRING=34
    WS=35
    COMMENT=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Function_argContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(nscParser.ID, 0)

        def getRuleIndex(self):
            return nscParser.RULE_function_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_arg" ):
                listener.enterFunction_arg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_arg" ):
                listener.exitFunction_arg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_arg" ):
                return visitor.visitFunction_arg(self)
            else:
                return visitor.visitChildren(self)




    def function_arg(self):

        localctx = nscParser.Function_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_function_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(nscParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self):
            return self.getTypedRuleContext(nscParser.StatementsContext,0)


        def getRuleIndex(self):
            return nscParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = nscParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nscParser.StatementContext)
            else:
                return self.getTypedRuleContext(nscParser.StatementContext,i)


        def getRuleIndex(self):
            return nscParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = nscParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4296320320) != 0):
                self.state = 46
                self.statement()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_statement(self):
            return self.getTypedRuleContext(nscParser.Assign_statementContext,0)


        def begin_end_statement(self):
            return self.getTypedRuleContext(nscParser.Begin_end_statementContext,0)


        def if_else_statement(self):
            return self.getTypedRuleContext(nscParser.If_else_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(nscParser.While_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(nscParser.For_statementContext,0)


        def loop_statement(self):
            return self.getTypedRuleContext(nscParser.Loop_statementContext,0)


        def print_simple(self):
            return self.getTypedRuleContext(nscParser.Print_simpleContext,0)


        def print_literal(self):
            return self.getTypedRuleContext(nscParser.Print_literalContext,0)


        def function_declration(self):
            return self.getTypedRuleContext(nscParser.Function_declrationContext,0)


        def getRuleIndex(self):
            return nscParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = nscParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.assign_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.begin_end_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.if_else_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 55
                self.while_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 56
                self.for_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 57
                self.loop_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 58
                self.print_simple()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 59
                self.print_literal()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 60
                self.function_declration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cumTerm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nscParser.CumTermContext)
            else:
                return self.getTypedRuleContext(nscParser.CumTermContext,i)


        def cumopr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nscParser.CumoprContext)
            else:
                return self.getTypedRuleContext(nscParser.CumoprContext,i)


        def getRuleIndex(self):
            return nscParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = nscParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.cumTerm()
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 132120576) != 0):
                self.state = 64
                self.cumopr()
                self.state = 65
                self.cumTerm()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CumTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nscParser.TermContext)
            else:
                return self.getTypedRuleContext(nscParser.TermContext,i)


        def additive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nscParser.AdditiveContext)
            else:
                return self.getTypedRuleContext(nscParser.AdditiveContext,i)


        def getRuleIndex(self):
            return nscParser.RULE_cumTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCumTerm" ):
                listener.enterCumTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCumTerm" ):
                listener.exitCumTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCumTerm" ):
                return visitor.visitCumTerm(self)
            else:
                return visitor.visitChildren(self)




    def cumTerm(self):

        localctx = nscParser.CumTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_cumTerm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.term()
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30 or _la==31:
                self.state = 73
                self.additive()
                self.state = 74
                self.term()
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nscParser.FactorContext)
            else:
                return self.getTypedRuleContext(nscParser.FactorContext,i)


        def multiplicative(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nscParser.MultiplicativeContext)
            else:
                return self.getTypedRuleContext(nscParser.MultiplicativeContext,i)


        def getRuleIndex(self):
            return nscParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = nscParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.factor()
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 939524096) != 0):
                self.state = 82
                self.multiplicative()
                self.state = 83
                self.factor()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exponent(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nscParser.ExponentContext)
            else:
                return self.getTypedRuleContext(nscParser.ExponentContext,i)


        def getRuleIndex(self):
            return nscParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = nscParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.exponent()
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 91
                self.match(nscParser.T__0)
                self.state = 92
                self.exponent()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExponentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return nscParser.RULE_exponent

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParenthesizedExpressionContext(ExponentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a nscParser.ExponentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(nscParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesizedExpression" ):
                listener.enterParenthesizedExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesizedExpression" ):
                listener.exitParenthesizedExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesizedExpression" ):
                return visitor.visitParenthesizedExpression(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierContext(ExponentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a nscParser.ExponentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(nscParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)


    class NumberContext(ExponentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a nscParser.ExponentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(nscParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)



    def exponent(self):

        localctx = nscParser.ExponentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_exponent)
        try:
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = nscParser.ParenthesizedExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.match(nscParser.T__1)
                self.state = 99
                self.expr()
                self.state = 100
                self.match(nscParser.T__2)
                pass
            elif token in [32]:
                localctx = nscParser.IdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.match(nscParser.ID)
                pass
            elif token in [33]:
                localctx = nscParser.NumberContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 103
                self.match(nscParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(nscParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(nscParser.ExprContext,0)


        def getRuleIndex(self):
            return nscParser.RULE_assign_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_statement" ):
                listener.enterAssign_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_statement" ):
                listener.exitAssign_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = nscParser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(nscParser.ID)
            self.state = 107
            self.match(nscParser.T__3)
            self.state = 108
            self.expr()
            self.state = 109
            self.match(nscParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Begin_end_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self):
            return self.getTypedRuleContext(nscParser.StatementsContext,0)


        def getRuleIndex(self):
            return nscParser.RULE_begin_end_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBegin_end_statement" ):
                listener.enterBegin_end_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBegin_end_statement" ):
                listener.exitBegin_end_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBegin_end_statement" ):
                return visitor.visitBegin_end_statement(self)
            else:
                return visitor.visitChildren(self)




    def begin_end_statement(self):

        localctx = nscParser.Begin_end_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_begin_end_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(nscParser.T__5)
            self.state = 112
            self.statements()
            self.state = 113
            self.match(nscParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_simpleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(nscParser.ID, 0)

        def getRuleIndex(self):
            return nscParser.RULE_print_simple

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_simple" ):
                listener.enterPrint_simple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_simple" ):
                listener.exitPrint_simple(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_simple" ):
                return visitor.visitPrint_simple(self)
            else:
                return visitor.visitChildren(self)




    def print_simple(self):

        localctx = nscParser.Print_simpleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_print_simple)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(nscParser.T__7)
            self.state = 116
            self.match(nscParser.ID)
            self.state = 117
            self.match(nscParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(nscParser.STRING, 0)

        def ID(self):
            return self.getToken(nscParser.ID, 0)

        def getRuleIndex(self):
            return nscParser.RULE_print_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_literal" ):
                listener.enterPrint_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_literal" ):
                listener.exitPrint_literal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_literal" ):
                return visitor.visitPrint_literal(self)
            else:
                return visitor.visitChildren(self)




    def print_literal(self):

        localctx = nscParser.Print_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_print_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(nscParser.T__7)
            self.state = 120
            self.match(nscParser.STRING)
            self.state = 121
            self.match(nscParser.T__8)
            self.state = 122
            self.match(nscParser.ID)
            self.state = 123
            self.match(nscParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(nscParser.ExprContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nscParser.StatementContext)
            else:
                return self.getTypedRuleContext(nscParser.StatementContext,i)


        def getRuleIndex(self):
            return nscParser.RULE_if_else_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_else_statement" ):
                listener.enterIf_else_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_else_statement" ):
                listener.exitIf_else_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_else_statement" ):
                return visitor.visitIf_else_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_else_statement(self):

        localctx = nscParser.If_else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_if_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(nscParser.T__9)
            self.state = 126
            self.expr()
            self.state = 127
            self.match(nscParser.T__10)
            self.state = 128
            self.statement()
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 129
                self.match(nscParser.T__11)
                self.state = 130
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(nscParser.ExprContext,0)


        def statement(self):
            return self.getTypedRuleContext(nscParser.StatementContext,0)


        def getRuleIndex(self):
            return nscParser.RULE_while_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_statement" ):
                listener.enterWhile_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_statement" ):
                listener.exitWhile_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_statement" ):
                return visitor.visitWhile_statement(self)
            else:
                return visitor.visitChildren(self)




    def while_statement(self):

        localctx = nscParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(nscParser.T__12)
            self.state = 134
            self.expr()
            self.state = 135
            self.match(nscParser.T__13)
            self.state = 136
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(nscParser.ID, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(nscParser.NUMBER)
            else:
                return self.getToken(nscParser.NUMBER, i)

        def statement(self):
            return self.getTypedRuleContext(nscParser.StatementContext,0)


        def getRuleIndex(self):
            return nscParser.RULE_for_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_statement" ):
                listener.enterFor_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_statement" ):
                listener.exitFor_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = nscParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(nscParser.T__14)
            self.state = 139
            self.match(nscParser.ID)
            self.state = 140
            self.match(nscParser.T__15)
            self.state = 141
            self.match(nscParser.NUMBER)
            self.state = 142
            self.match(nscParser.T__16)
            self.state = 143
            self.match(nscParser.NUMBER)
            self.state = 144
            self.match(nscParser.T__13)
            self.state = 145
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(nscParser.ID, 0)

        def NUMBER(self):
            return self.getToken(nscParser.NUMBER, 0)

        def statement(self):
            return self.getTypedRuleContext(nscParser.StatementContext,0)


        def getRuleIndex(self):
            return nscParser.RULE_loop_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop_statement" ):
                listener.enterLoop_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop_statement" ):
                listener.exitLoop_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_statement" ):
                return visitor.visitLoop_statement(self)
            else:
                return visitor.visitChildren(self)




    def loop_statement(self):

        localctx = nscParser.Loop_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_loop_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(nscParser.T__17)
            self.state = 148
            self.match(nscParser.ID)
            self.state = 149
            self.match(nscParser.T__18)
            self.state = 150
            self.match(nscParser.NUMBER)
            self.state = 151
            self.match(nscParser.T__13)
            self.state = 152
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declrationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(nscParser.ID, 0)

        def begin_end_statement(self):
            return self.getTypedRuleContext(nscParser.Begin_end_statementContext,0)


        def function_arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nscParser.Function_argContext)
            else:
                return self.getTypedRuleContext(nscParser.Function_argContext,i)


        def getRuleIndex(self):
            return nscParser.RULE_function_declration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_declration" ):
                listener.enterFunction_declration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_declration" ):
                listener.exitFunction_declration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declration" ):
                return visitor.visitFunction_declration(self)
            else:
                return visitor.visitChildren(self)




    def function_declration(self):

        localctx = nscParser.Function_declrationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_function_declration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(nscParser.T__19)
            self.state = 155
            self.match(nscParser.ID)
            self.state = 156
            self.match(nscParser.T__1)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 162
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 157
                        self.function_arg()
                        self.state = 158
                        self.match(nscParser.T__8) 
                    self.state = 164
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                self.state = 165
                self.function_arg()


            self.state = 168
            self.match(nscParser.T__2)
            self.state = 169
            self.begin_end_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CumoprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return nscParser.RULE_cumopr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCumopr" ):
                listener.enterCumopr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCumopr" ):
                listener.exitCumopr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCumopr" ):
                return visitor.visitCumopr(self)
            else:
                return visitor.visitChildren(self)




    def cumopr(self):

        localctx = nscParser.CumoprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_cumopr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 132120576) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return nscParser.RULE_multiplicative

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicative" ):
                listener.enterMultiplicative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicative" ):
                listener.exitMultiplicative(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicative" ):
                return visitor.visitMultiplicative(self)
            else:
                return visitor.visitChildren(self)




    def multiplicative(self):

        localctx = nscParser.MultiplicativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_multiplicative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 939524096) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return nscParser.RULE_additive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditive" ):
                listener.enterAdditive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditive" ):
                listener.exitAdditive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditive" ):
                return visitor.visitAdditive(self)
            else:
                return visitor.visitChildren(self)




    def additive(self):

        localctx = nscParser.AdditiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_additive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            _la = self._input.LA(1)
            if not(_la==30 or _la==31):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





