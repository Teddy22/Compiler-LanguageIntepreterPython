from StatementList import StatementList
from Interface_mod import NullException


class StatementBlock:

    def __init__(self, statement_list):
        if statement_list is None:
            raise NullException('null argument for StatementList argument  at ' + self.__name__)
        if not isinstance(statement_list, StatementList):
            raise Exception('invalid type for StatementList argument at ' + self.__name__)

        self.statements_list = statement_list

    def execute(self):
        self.statements_list.execute()