from copy import deepcopy
class Pole():
    def __init__(self):
        object.__init__(self)
    p=[['  ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', '  '],
        ['  ', '-', '-', '-', '-', '-', '-', '-', '-' '  '],
        ['8 ', '*', '⛂', '*', '⛂', '*', '⛂', '*', '⛂', ' 8'],
        ['7 ', '⛂', '*', '⛂', '*', '⛂', '*', '⛂', '*', ' 7'],
        ['6 ', '*', '⛂', '*', '⛂', '*', '⛂', '*', '⛂', ' 6'],
        ['5 ', '*', '*', '*', '*', '*', '*', '*', '*', ' 5'],
        ['4 ', '*', '*', '*', '*', '*', '*', '*', '*', ' 4'],
        ['3 ', '⛀', '*', '⛀', '*', '⛀', '*', '⛀', '*', ' 3'],
        ['2 ', '*', '⛀', '*', '⛀', '*', '⛀', '*', '⛀', ' 2'],
        ['1 ', '⛀', '*', '⛀', '*', '⛀', '*', '⛀', '*', ' 1'],
        ['  ', '-', '-', '-', '-', '-', '-', '-', '-' '  '],
        ['  ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', '  ']]
    k1, k2, k3={'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}, 'ABCDEFGH', '12345678' #b=k1, k=k2, k1=k3
    f={'⛁':'D','⛃':'d', '⛀':'S','⛂':'s', '*':'*'}
    fi={'⛁': 'D', '⛃': 'd', '⛀': 'S', '⛂': 's'}
    def print(self):
        if self.HOD % 2 != 0:
            print(f'\nХод номер {self.HOD}\nХодит первый(нижний) игрок\n')
        else:
            print(f'\nХод номер {self.HOD}\nХодит второй(верхний) игрок\n')
        for i in self.p:
            print(*i)
    def Vb(self, p):  #Основная функция
        if p==0:
            self.print()
            self.s = input('\nЧерез пробел введите координаты выбранной фигуры и координаты клетки, в которую хотите сходить (если хотите вернуться на N ходов назад, то введите N): ').upper()
        elif p==1:
            self.s = input('Данные введены неверно, повторите попытку: ').upper()
        elif p==2:
            self.s = input(f'Данные введены неверно (максимальное число "откатов": {self.HOD - 1}), повторите попытку: ').upper()
        elif p==3:
            self.s = input(f'Фигура так сходить не может, повторите попытку: ').upper()
        elif p==4:
            self.s = input('Данные введены неверно (сейчас ходит другой игрок), повторите попытку: ').upper()
        elif p==5:
            self.s = input('Данные введены неверно (в клетке стоит союзная фигура), повторите попытку: ').upper()
        else:
            self.print()
            self.s = input('Вы можете сделать еще ход этой фигурой, через пробел введите координаты выбранной фигуры и координаты клетки, \nв которую хотите сходить (если хотите вернуться на N ходов назад, то введите N): ').upper()
        if self.s.isdigit():
            return self.rev(self.s)
        else:
            self.s = self.s.split(' ')
            return self.vb()
    def vb(self):  #Проверяет выбранную фигуру
        if len(self.s) == 2:
            if self.s[0][0] not in self.k2 or self.s[-1][0] not in self.k2 or self.s[0][-1] not in self.k3 or self.s[-1][-1] not in self.k3 or \
                    self.p[10-int(self.s[0][-1])][self.k1[self.s[0][0]]]=='*':
                return self.Vb(1)
            else:
                p1, p2 = self.f[self.p[10 - int(self.s[0][-1])][self.k1[self.s[0][0]]]].islower(), self.f[self.p[10 - int(self.s[-1][-1])][self.k1[self.s[-1][0]]]].islower()
                if self.p[10 - int(self.s[-1][-1])][self.k1[self.s[-1][0]]]!='*' and p1 == p2:
                    return self.Vb(5)
                elif (self.HOD%2!=0 and p1==True) or (self.HOD%2==0 and p1==False):
                    return self.Vb(4)
                return self.fig([[10-int(self.s[0][-1]), self.k1[self.s[0][0]]], [10-int(self.s[-1][-1]), self.k1[self.s[-1][0]]]])
        else:
            return self.Vb(1)
    def rev(self, x):
        if x.isdigit() and int(x)>=0 and int(x)<=self.HOD-1:
            self.p=self.HODS[len(self.HODS)-int(x)-1][-1]
            self.HOD -= int(x)
            self.HODS = deepcopy(self.HODS)[:self.HOD]
            print(f'\nПроизошел "откат" на {int(x)} ход(-a/-ов)')
            return self.Vb(0)
        return self.Vb(2)
    HODS, HOD = [], 1
    def game(self):
        while self.mat():
            g=deepcopy(self.p)
            self.HODS += [[self.HOD, g]]
            self.Vb(0)
            self.HOD += 1
        print(f'\nИгрок {self.HOD%2+1} победил, поставив мат игроку номер {self.HOD%2}\nКоличество ходов: {self.HOD-1}')
    def fig(self, x):
        self.h=x
        self.X=globals()[self.f[self.p[x[0][0]][x[0][-1]]].lower()]
        if self.X.HOD(self):
            return self.Xodi()
        else:
            self.Vb(3)
    def prov(self):
        if self.h[-1][0]+2<=9:
            if self.h[-1][-1]+2<=8 and self.p[self.h[-1][0]+1][self.h[-1][-1]+1]!='*':
                if self.p[self.h[-1][0]+2][self.h[-1][-1]+2]=='*' and self.fi[self.p[self.h[-1][0]][self.h[-1][-1]]].islower()!=self.fi[self.p[self.h[-1][0]+1][self.h[-1][-1]+1]].islower():
                    return self.Vb(6)
            elif self.h[-1][-1]-2>=1 and self.p[self.h[-1][0]+1][self.h[-1][-1]-1]!='*':
                if self.p[self.h[-1][0]+2][self.h[-1][-1]-2]=='*' and self.fi[self.p[self.h[-1][0]][self.h[-1][-1]]].islower()!=self.fi[self.p[self.h[-1][0]+1][self.h[-1][-1]-1]].islower():
                    return self.Vb(6)
        elif self.h[-1][0]-2>=2:
            if self.h[-1][-1]+2<=8 and self.p[self.h[-1][0]+1][self.h[-1][-1]+1]!='*':
                if self.p[self.h[-1][0]-2][self.h[-1][-1]+2]=='*' and self.fi[self.p[self.h[-1][0]][self.h[-1][-1]]].islower()!=self.fi[self.p[self.h[-1][0]-1][self.h[-1][-1]+1]].islower():
                    return self.Vb(6)
            elif self.h[-1][-1]-2>=1 and self.p[self.h[-1][0]+1][self.h[-1][-1]-1]!='*':
                if self.p[self.h[-1][0]-2][self.h[-1][-1]-2]=='*' and self.fi[self.p[self.h[-1][0]][self.h[-1][-1]]].islower()!=self.fi[self.p[self.h[-1][0]-1][self.h[-1][-1]-1]].islower():
                    return self.Vb(6)

    def Xodi(self):
        self.p[self.h[-1][0]][self.h[-1][-1]]=self.p[self.h[0][0]][self.h[0][-1]]
        self.p[self.h[0][0]][self.h[0][-1]]='*'
        if self.h[-1][0] == 2 and self.f[self.p[self.h[-1][0]][self.h[-1][-1]]].isupper():
            self.p[self.h[-1][0]][self.h[-1][-1]]='⛁'
        elif self.h[-1][0] == 9 and self.f[self.p[self.h[-1][0]][self.h[-1][-1]]].islower():
            self.p[self.h[-1][0]][self.h[-1][-1]]='⛃'
        if abs(self.h[0][0] - self.h[-1][0]) == abs(self.h[0][-1] - self.h[-1][-1]) == 2:
            self.prov()
    def mat(self):
        return True

class s(Pole):
    def __init__(self):
        Pole.__init__(self)
    def HOD(self):
        if abs(self.h[0][0]-self.h[-1][0])==abs(self.h[0][-1]-self.h[-1][-1])==1 and self.p[self.h[-1][0]][self.h[-1][-1]]=='*':
            if self.f[self.p[self.h[0][0]][self.h[0][-1]]]=='s' and self.h[0][0]>=self.h[-1][0]:
                return False
            if self.f[self.p[self.h[0][0]][self.h[0][-1]]]=='S' and self.h[0][0]<=self.h[-1][0]:
                return False
            return True
        elif abs(self.h[0][0]-self.h[-1][0])==abs(self.h[0][-1]-self.h[-1][-1])==2 and self.p[self.h[-1][0]][self.h[-1][-1]]=='*':
            if self.h[0][-1]<self.h[-1][-1]:
                if self.h[0][0]<self.h[-1][0]:
                    if self.p[self.h[0][0]][self.h[0][-1]]!=self.p[self.h[0][0]+1][self.h[0][-1]+1]:
                        self.p[self.h[0][0] + 1][self.h[0][-1] + 1]='*'
                        return True
                else:
                    if self.p[self.h[0][0]][self.h[0][-1]]!=self.p[self.h[0][0]-1][self.h[0][-1]+1]:
                        self.p[self.h[0][0] - 1][self.h[0][-1] + 1]='*'
                        return True
            else:
                if self.h[0][0]<self.h[-1][0]:
                    if self.p[self.h[0][0]][self.h[0][-1]]!=self.p[self.h[0][0] + 1][self.h[0][-1] - 1]:
                        self.p[self.h[0][0] + 1][self.h[0][-1] - 1]='*'
                        return True
                else:
                    if self.p[self.h[0][0]][self.h[0][-1]]!=self.p[self.h[0][0] - 1][self.h[0][-1] - 1]:
                        self.p[self.h[0][0] - 1][self.h[0][-1] - 1]='*'
                        return True
        return False

class d(Pole):
    def __init__(self):
        Pole.__init__(self)
    def HOD(self):
        k=0
        pp=deepcopy(self.p)
        if abs(self.h[0][0] - self.h[-1][0]) == abs(self.h[0][-1] - self.h[-1][-1]) and self.p[self.h[-1][0]][self.h[-1][-1]]=='*':
            for i in range(min(self.h[0][0], self.h[-1][0]) + 2, max(self.h[0][0], self.h[-1][0])):
                if self.h[0][-1] < self.h[-1][-1]:
                    if self.p[i][self.h[-1][-1] - (i % min(self.h[0][0], self.h[-1][0]))] != '*':
                        k+=1
                        pp[i][self.h[-1][-1] - (i % min(self.h[0][0], self.h[-1][0]))]='*'
            if k <= 1:
                self.p = deepcopy(pp)
                return True
            for i in range(min(self.h[0][0], self.h[-1][0]) + 2, max(self.h[0][0], self.h[-1][0])):
                if self.h[0][-1] > self.h[-1][-1]:
                    if self.p[i][self.h[-1][-1] + (i % min(self.h[0][0], self.h[-1][0]))] != '*':
                        k+=1
                        pp[i][self.h[-1][-1] + (i % min(self.h[0][0], self.h[-1][0]))]='*'
            if k<=1:
                self.p = deepcopy(pp)
                return True
        return False

a=Pole()
a.game()