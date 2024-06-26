# Generated from nsc.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .nscParser import nscParser
else:
    from nscParser import nscParser

# This class defines a complete generic visitor for a parse tree produced by nscParser.

class nscVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by nscParser#function_arg.
    def visitFunction_arg(self, ctx:nscParser.Function_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#program.
    def visitProgram(self, ctx:nscParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#statements.
    def visitStatements(self, ctx:nscParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#statement.
    def visitStatement(self, ctx:nscParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#expr.
    def visitExpr(self, ctx:nscParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#comparisonTerm.
    def visitComparisonTerm(self, ctx:nscParser.ComparisonTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#term.
    def visitTerm(self, ctx:nscParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#factor.
    def visitFactor(self, ctx:nscParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#ParenthesizedExpression.
    def visitParenthesizedExpression(self, ctx:nscParser.ParenthesizedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#Identifier.
    def visitIdentifier(self, ctx:nscParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#Number.
    def visitNumber(self, ctx:nscParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#FunctionCall.
    def visitFunctionCall(self, ctx:nscParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#UnaryMinus.
    def visitUnaryMinus(self, ctx:nscParser.UnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#function_call.
    def visitFunction_call(self, ctx:nscParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#assign_statement.
    def visitAssign_statement(self, ctx:nscParser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#begin_end_statement.
    def visitBegin_end_statement(self, ctx:nscParser.Begin_end_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#print_simple.
    def visitPrint_simple(self, ctx:nscParser.Print_simpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#print_literal.
    def visitPrint_literal(self, ctx:nscParser.Print_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#if_else_statement.
    def visitIf_else_statement(self, ctx:nscParser.If_else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#while_statement.
    def visitWhile_statement(self, ctx:nscParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#for_statement.
    def visitFor_statement(self, ctx:nscParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#loop_statement.
    def visitLoop_statement(self, ctx:nscParser.Loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#function_declration_statement.
    def visitFunction_declration_statement(self, ctx:nscParser.Function_declration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#function_call_statement.
    def visitFunction_call_statement(self, ctx:nscParser.Function_call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#return_statement.
    def visitReturn_statement(self, ctx:nscParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#comparisonopr.
    def visitComparisonopr(self, ctx:nscParser.ComparisonoprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#multiplicative.
    def visitMultiplicative(self, ctx:nscParser.MultiplicativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nscParser#additive.
    def visitAdditive(self, ctx:nscParser.AdditiveContext):
        return self.visitChildren(ctx)



del nscParser