# expr_visitor.py

from grammar.nscParser import nscParser


class NscVisitorImpl:
    def visitUnaryMinus(self, ctx):
        return -self.visit(ctx.expr())

    def visitFactor(self, ctx: nscParser.ExponentContext) -> int | float:
        exponents = ctx.exponent()

        values: list[int] = list(map(self.visit, exponents))
        while len(values) > 1:
            a = values.pop()
            b = values.pop()
            values.append(b ** a)
        return values[0]

    def visitTerm(self, ctx: nscParser.MultiplicativeContext):
        factors = ctx.factor()
        left = self.visit(factors[0])
        if len(factors) < 2:
            return left

        for d, c in enumerate(ctx.multiplicative()):
            right: int = self.visit(factors[d+1])
            opr = c.getText()
            if opr == '*':
                left *= right
            elif opr == '/':
                left /= right
            else:
                left %= right
        return left

    def visitParenthesizedExpression(self, ctx: nscParser.ParenthesizedExpressionContext):
        return self.visit(ctx.expr())

    def visitNumber(self, ctx: nscParser.NumberContext):
        return self.strToNumber(ctx.NUMBER().getText())

    def visitExponent(self, ctx) -> int | float:
        if isinstance(ctx, nscParser.NumberContext):
            return self.visit(ctx)
        elif isinstance(ctx, nscParser.IdentifierContext):
            return self.visit(ctx)
        # elif isinstance(ctx, nscParser.UnaryMinusContext):
        #     return self.visitUnaryMinus(ctx)
        elif isinstance(ctx, nscParser.ParenthesizedExpressionContext):
            return self.visit(ctx)
        
        elif isinstance(ctx, nscParser.FunctionCallContext):
            return self.visit(ctx)

    def getBool(self, left, right, op):
        if op == '<':
            return left < right
        elif op == '>':
            return left > right
        elif op == '<=':
            return left <= right
        elif op == '>=':
            return left >= right
        elif op == '==':
            return left == right
        elif op == '!=':
            return left != right

    def visitExpr(self, ctx):
        comparisonterms = list(map(self.visit, ctx.comparisonTerm()))
        left = comparisonterms[0]
        if len(comparisonterms) < 2:
            return left
        for d, c in enumerate(ctx.comparisonopr()):
            left = self.getBool(left, comparisonterms[d + 1], c.getText())
        return left

    def visitComparisonTerm(self, ctx):
        if ctx is None:
            return 0
        terms = ctx.term()
        left = self.visit(terms[0])
        if len(terms) < 2:
            return left
        # right = self.visitTerm(terms[1])
        for d, c in enumerate(ctx.additive()):
            right = self.visit(terms[d + 1])
            if c.getText() == '+':
                left += right
            else:
                left -= right
        return left
