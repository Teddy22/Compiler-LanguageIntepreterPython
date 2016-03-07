from StatementBlock import StatementBlock
from Interface_mod import NullException


class Program:

    def __init__(self, block):
        if block is None:
            raise NullException('null statement block argument at ' + self.__name__)
        if not isinstance(block, StatementBlock):
            raise TypeError('invalid type for statement block argument at ' + self.__name__)

        self.block = block

    def execute(self):
        self.block.execute()