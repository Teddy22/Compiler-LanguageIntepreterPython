from Interface_mod import Statement
from BooleanExpression import BooleanExpression
from StatementBlock import StatementBlock


class IfStatement(Statement):

    def __init__(self):
        self.expr_list = []
        self.block_list = []

    def add_expression(self, bool_expr):
        if bool_expr is None:
            raise Exception('null boolean expression at If Statement')
        if not isinstance(bool_expr, BooleanExpression):
            raise TypeError('invalid type for BooleanExpression argument at If Statement')

        self.expr_list.append(bool_expr)

    def add_block(self, block):
        if not isinstance(block, StatementBlock):
            raise TypeError('invalid type for StatementBlock argument at If Statement')

        self.block_list.append(block)

    def execute(self):
        if len(self.block_list) == 0:
            raise RuntimeError('illegal if statement - no statement blocks found')
        if len(self.expr_list) == 0:
            raise RuntimeError('illegal if statement - no expressions found')
        if len(self.block_list) != len(self.expr_list) + 1:
            raise RuntimeError('illegal if statement - unexpected number of boolean'
                               'expressions or blocks')

        true_found = False
        for i in range(0, len(self.expr_list)):
            if self.expr_list[i].evaluate():
                true_found = True
                break

        if true_found:
            self.block_list[i].execute()
        else:
            self.block_list[len(self.block_list)-1].execute()


