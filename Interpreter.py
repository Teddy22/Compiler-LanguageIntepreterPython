from Interface_mod import LexicalException
from Interface_mod import ParserException
from Parser import Parser


def main():
    try:
        print('-------------------test file 1-------------------------------')
        parser1 = Parser('test1.py')
        program1 = parser1.parse()
        program1.execute()
        print('-------------------test file 1 end-------------------------------\n\n')

        print('-------------------test file 2-------------------------------')
        parser2 = Parser('test2.py')
        program2 = parser2.parse()
        program2.execute()
        print('-------------------test file 2 end-------------------------------\n\n')

        print('-------------------test file 3-----------------------------------')
        parser3 = Parser('test3.py')
        program3 = parser3.parse()
        program3.execute()
        print('-------------------test file 3 end-------------------------------\n\n')

        print('-------------------test file 4-------------------------------')
        parser4 = Parser('test4.py')
        program4 = parser4.parse()
        program4.execute()
        print('-------------------test file 4 end-------------------------------')


    except FileNotFoundError as e:
        print(e)
    except LexicalException as e:
        print(e)
    except ParserException as e:
        print(e)
    except Exception as e:
        print('unexpected error occurred at interpreter -', e)

if __name__ == '__main__':
    main()