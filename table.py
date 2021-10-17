class Table:
    def __init__(self, function):
        self.function = function
        self.headers = list(self.function.__code__.co_varnames)
        self.signs = {'not': '¬', 'or' : '∨', 'and' : '∧', 'column' : '|', 'row' : '-'}
        self._column_size = len(max(self.headers, key=lambda x: len(x))) + 2

        self.ans = []
        self.dnf = []
        self.denial = {}

    def separator(self, length: int):
        return self.signs['row'] * length

    def row(self, *args):
        r = ''
        for name in args:
            r += f'''{self.signs['column']}{name:^{self._column_size}}'''
        return r + self.signs['column']

    def header(self):
        return self.row(*(self.headers + ['F']))