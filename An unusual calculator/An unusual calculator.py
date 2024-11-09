from num2words import * #Преобразование чисел в слова(только в И.п.)
kl1 = [] #Список для преобразования слов в числа(только в И.п.)
znam={'первых':1,'вторых':2,'третьих':3,'четвертых':4,'пятых':5,'шестых':6,'седьмых':7,\
      'восьмых':8,'девятых':9,'десятых':10,'одиннадцатых':11,'двенадцатых':12,'тринадцатых':13,\
      'четырнадцатых':14,'пятнадцатых':15,'шестнадцатых':16,'семнадцатых':17,'восемнадцатых':18,\
      'девятнадцатых':19,'двадцатых':20,'тридцатых':30,'сороковых':40,'пятидесятых':50,\
      'шестидесятых':60,'семидесятых':70,'восьмидесятых':80,'девяностых':90} #Словарь для перевода знаменателя дроби в число
for i in range(100):
    kl1+=[(num2words(i, lang='ru'), i)]
d = dict(kl1) #Словарь реобразованых чисел в слова(только в И.п.)
# print(num2words(1, lang='ru'))
# print(d['один'])
znamO={} #Словарь для перевода знаменателя дроби в слово для ответа
for i2 in znam:
    znamO[str(znam[i2])]=i2
def DROB(x, y): #находим общий знаменатель дробей
    if len(x)==len(y)==2: #если обе дроби
        x[0]*=y[-1] #домножаем первый числитель
        y[0]*=x[-1] #домножаем второй числитель
        y[-1]*=x[-1]#получаем общий знаменатель
        x[-1]=y[-1]
    else: #если только одна дробь
        if len(x)==1:
            x[0]*=y[-1]
        else:
            y[0]*=x[-1]
            y+=[x[-1]]
    return [x, y]
def drob(x): #переводим каждую часть в число
    drob1=x.split()
    droob=[] #дробь, в которой есть числитель и знаменатель
    if len(drob1)==1: #если число из одного слова
        return [d[drob1[0]]]
    elif len(drob1)>1 and drob1[0] in d and drob1[-1] not in znam: #если число из двух слов
        return [d[drob1[0] + ' ' + drob1[-1]]]
    if 'и' in drob1: #если дробь смешанная
        cm=drob1[:drob1.index('и')]
        if len(cm)==1: #если 
            droob+=[d[cm[0]]]
        else:
            droob+=[int(str(d[cm[-2]]//10) + str(d[cm[-1]]))]
        drob1=drob1[drob1.index('и')+1:]
        if len(drob1)==2:
            droob+=[int(str(d[drob1[-2]]))]
            droob+=[int(str(znam[drob1[-1]]))]
        elif len(drob1)==4:
            droob+=[int(str(d[drob1[0]]//10) + str(d[drob1[1]]))]
            droob+=[int(str(d[drob1[-2]]//10) + str(znam[drob1[-1]]))]
        elif len(drob1)==3:
            if (str(drob1[0]) + ' ' + str(drob1[1])) in d:
                droob+=[int(str(d[drob1[0]]//10) + str(d[drob1[1]]))]
                droob+=[znam[drob1[-1]]]
            else:
                droob+=[d[drob1[0]]]
                droob+=[int(str(d[drob1[-2]]//10) + str(znam[drob1[-1]]))]
    else: #если дробь обыкновенная
        if len(drob1)==2:
            droob+=[d[drob1[0]]]
            droob+=[znam[drob1[-1]]]
        elif len(drob1)==4:
            droob+=[int(str(d[drob1[0]]//10) + str(d[drob1[1]]))]
            droob+=[int(str(d[drob1[-2]]//10) + str(znam[drob1[-1]]))]
        elif len(drob1)==3:
            if (str(drob1[0]) + ' ' + str(drob1[1])) in d:
                droob+=[int(str(d[drob1[0]]//10) + str(d[drob1[1]]))]
                droob+=[znam[drob1[-1]]]
            else:
                droob+=[d[drob1[0]]]
                droob+=[int(str(d[drob1[-2]]//10) + str(znam[drob1[-1]]))]
    if len(droob)==3: #переводим неправильную дробь
        droob[1]=droob[-1]*droob[0]+droob[1] 
    return droob[-2:] #выводим числитель и знаменатель правильной дроби
def otv(x): #Преобразование ответа в слова
    s=''
    if x[0]<x[-1]: #Записываем числитель или целую часть
        s+= num2words(x[0], lang='ru')
    elif x[0]==x[-1]:
        return 'один'
    else:
        if x[0]%x[-1]!=0:
            s=s + num2words(x[0]//x[-1], lang='ru') + ' и ' + num2words(x[0]-x[-1]*(x[0]//x[-1]), lang='ru')
        else:
            return num2words(x[0]//x[-1], lang='ru')
    if x[-1]==1:
        return num2words(x[0], lang='ru')
    else:
        x1=str(x[-1])
        if x1 in znamO:
            s=s + ' ' + znamO[x1]
        elif x[-1]>20 and x[-1]<=99:
            s=s + ' ' + num2words(str((int(x1))//10) + '0', lang='ru') + ' ' + znamO[x1[-1]]
        elif x[-1]>100 and x[-1]<110:
            s=s + ' сто ' + znamO[x1[2:]]
        elif x[-1]>=110 and x[-1]<=120:
            s=s + ' сто ' + znamO[x1[1:]]
        elif x[-1]>120 and x[-1]<1000:
            s=s + ' '  + num2words(str((int(x[-1])//100)) + '00', lang='ru') + ' ' + \
               num2words(str((int(x1[1:])//10)) + '0', lang='ru') + ' ' + znamO[x1[-1]]
        elif x[-1]>1000 and x[-1]<10000:
            s=s + ' '  + num2words(str((int(x[-1])//1000)) + '000', lang='ru') + ' ' + \
               num2words(str((int(x1[1:])//100)) + '00', lang='ru') + ' ' + \
               num2words(str((int(x1[2:])//10)) + '0', lang='ru') + ' ' + znamO[x1[-1]]
    return s 
def calc(s):
    if ' плюс ' in s:
        s=s.split(' плюс ')
        s1, s2=drob(s[0]), drob(s[1])
        if len(s1)==2 or len(s2)==2:
            q=DROB(s1, s2)
            q[-1][0]=q[0][0]+q[-1][0]
            return otv(q[-1])
        else:
            return num2words(int(s1[0])+int(s2[0]), lang='ru')
    elif ' минус' in s:
        s=s.split(' минус ')
        s1, s2=drob(s[0]), drob(s[1])
        if len(s1)==2 or len(s2)==2:
            q=DROB(s1, s2)
            q[-1][0]=q[0][0]-q[-1][0]
            return otv(q[-1])
        else:
            return num2words(int(s1[0])-int(s2[0]), lang='ru')
    elif ' умножить на ' in s:
        s=s.split(' умножить на ')
        s1, s2=drob(s[0]), drob(s[1])
        if len(s1)==2 and len(s2)==2: #Перемножение дробей производится во вторую дробь
            s2[0]*=s1[0]
            s2[-1]*=s1[-1]
        if len(s1)==1 and len(s2)==1:
            return num2words(int(s1[0])*int(s2[0]), lang='ru')
        if len(s1)==1 or len(s2)==1:
            if len(s1)==1:
                s2[0]*=s1[0]
            else:
                s1[0]*=s2[0]
                s2[0]=s1[0]
                s2+=[s1[1]]
        return otv(s2)
t=input('Введите ваш пример: ')
print('Ответ:', calc(t))


