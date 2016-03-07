from Interface_mod import NullException


class Memory:

    mem = {}

    def __init__(self):

        chars = []
        values = []

        for i in range(0, 26):
            chars.append(chr(97 + i))
        for i in range(0, 26):
            chars.append(chr(65 + i))
        for i in range(0, 52):
            values.append(None)

        self.mem = dict(zip(chars, values))

    @staticmethod
    def fetch(char):

        if not isinstance(char, str):
            raise TypeError('invalid character argument at Memory')
        if not char.isalpha() or len(char) != 1:
            raise TypeError('invalid character argument at Memory')

        try:
            mem = Memory.mem[char]
        except KeyError as e:
            raise NullException('undefined identifier ' + char)
        except Exception as e:
            raise MemoryError('Memory error occurred in relation to identifier ' + char)

        return Memory.mem[char]

    @staticmethod
    def store(char, value):
        if char is None:
            raise NullException('Null char argument value at Memory.store')
        if value is None:
            raise NullException('Null value argument at Memory.store')
        if not isinstance(char, str):
            raise TypeError('invalid character argument at Memory')
        if not char.isalpha() or len(char) != 1:
            raise TypeError('invalid character argument at Memory')
        if not isinstance(value, int):
            raise TypeError('invalid integer value argument at Memory')

        Memory.mem[char] = value









