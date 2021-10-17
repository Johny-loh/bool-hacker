from table import Table
from function import long_running3 as func

class Bool_hacker(Table):

    def inversion(self):
        for i in self.headers:
            self.denial[i] = self.signs['not'] + i
            self.denial[self.signs['not'] + i] = i
    
    def creator(self):
        header = self.header()
        separetor = self.separator(len(header))
        print(separetor)
        print(header)
        print(separetor)

    def bool_hack(self):
        for i in range(2 ** len(self.headers)):
            d = list(map(int, bin(i)[2:].zfill(len(self.headers))))

            res = self.row(*(d + [self.function(*d)]))
            if self.function(*d):
                self.ans.append(d)
            print(res)

    def sdnf(self, mode=1): #Создаем Соверешенный ДНФ стандартным путем
        count = 0
        a = ''
        for i in range(len(self.ans)):
            self.dnf.append(set())
            for j in range(len(self.ans[i])):
                a += self.signs['not'] * (1 - int(self.ans[i][j])) + self.headers[j]
                self.dnf[-1].add(self.signs['not'] * (1 - int(self.ans[i][j])) + self.headers[j])

            a += " + " * (1 - (i + 1) // len(self.ans))
        if a != '':
            print('SDNF...', a, sep='\n')

            # count += 1
            # if mode:
            #     print(f" {self.signs['and']} ".join(self.dnf[-1]) + (' ' + self.signs['or'] + ' ') * (1 - count // len(self.ans)), end='')
            # else:
            #     print("".join(self.dnf[-1]) + ' + ' * (1 - count // len(self.ans)), end='')

    def check(self, *args):
        if args[0] == args[1]:
            return (1, None, None)

        elif len(args[0]) == 1 and len(args[1]) == 1:
            if self.denial[list(args[0])[0]] in args[1]:
                return (2, None, None)
            else:
                return (-1, None, None)

        elif len(args[0]) == 0 or len(args[1]) == 0:
            return (2, None, None)

        elif len(args[0]) + len(args[1]) == 3:
            ab, b = sorted(args, key=len)
            for i in ab:
                c = {self.denial[i]}
                if self.denial[i] in b:
                    return (3, ab, b.difference(c))
                else:
                    return (-1, None, None)
        else:
            return (-1, None, None)

    def reduction(self, example : list):    # Основной цикл для сокращения : перебор и сравнение всех частей выражений
        print('\nSolution DNF...')
        i = 0
        j = 1
        # for _ in example:
        #     print("".join(sorted(_, key=lambda x: x[-1])), end=' + ')
        # print('------------')
        while i < len(example) - 1:
            while j < len(example):
                mode, attr1, attr2 = self.check(example[i].difference(example[j]), example[j].difference(example[i]))
                if mode == 1: #Убираем повторение
                    del example[j]
                    # for _ in example:
                    #     print("".join(sorted(_, key=lambda x: x[-1])), end=' + ')
                    # print('------------', mode, i, j)
                    i = 0
                    j = 0
                elif mode == 2: #Исключение третьего или же поглащение
                    example[i] = example[i].intersection(example[j])
                    del  example[j]
                    # for _ in example:
                    #     print("".join(sorted(_, key=lambda x: x[-1])), end=' + ')
                    # print('------------', mode, i, j)
                    i = 0
                    j = 0
                elif mode == 3: #Метод кого-то ¬a+ab = ¬a+b
                    b = example[i]
                    c = example[j]
                    example[i] = (b.intersection(c)).union(attr1)
                    example[j] = (c.intersection(b)).union(attr2)
                    # for _ in example:
                    #     print("".join(sorted(_, key=lambda x: x[-1])), end=' + ')
                    # print('------------', mode, i, j)
                    i = 0
                    j = 0

                j += 1
            i += 1
            j = i + 1

        b = ''
        for i in range(len(example)):
            b += ''.join(sorted(example[i], key=lambda x: x[-1])) + ' + ' * (1 - (i + 1) // len(example))
        if b == '':
            return 1
        return b

    def streak(self):
        print('\nRemove to streak...')
        a = self.dnf
        if a[0] == set():
            a = list(self.headers)
            b = ''
            for i in range(len(a)):
                b +=  a[i] + '|' * (1 - (i + 1) // len(a))
            return f'({b})|(({b})|({b})) == 1'

        for i in range(len(a)):
            a[i] = list(a[i])
            for j in range(len(a[i])):
                if '¬' in a[i][j]:
                    a[i][j] = f'({a[i][j][-1]}|{a[i][j][-1]})'

            if len(a) == 1 and len(a[0]) == 1:
                return ''.join(a[0])
            b = ''
            for j in range(len(a[i])):
                b += a[i][j] + "|" * (1 - (j + 1) // len(a[i]))
            a[i] = '(' + '(' + b + ')' + '|' + '(' + b + ')' + ')'

        c = ''
        for i in range(len(a) - 1):
            c += '(' + a[i] + '|' + a[i] + ')' + '|' + '(' + a[i + 1] + '|' + a[i + 1] + ')' + "|" * (1 - (i + 1) // (len(a) - 1))

        if len(a) == 1:
            return ''.join(a)

        return c

    def main(self):
        self.creator()
        self.bool_hack()
        self.sdnf(0)
        self.inversion()
        if len(self.dnf) != 0:
            print(self.reduction(self.dnf))
            print(self.streak())

Bool_hacker(func).main()