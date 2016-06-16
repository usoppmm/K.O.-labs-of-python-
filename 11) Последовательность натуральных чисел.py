from itertools import product
from functools import reduce
numbers = input().split(' ')
signs = ['+','-']
combinations = list(product(signs, repeat=len(numbers)-2)) # аналог вложенных циклов
stop = False

for combination in combinations:
    for i, number in enumerate(numbers[:-1]): # счетчик
        c = list(combination[:])
        c.insert(i, '==')
        equation = ''.join(reduce(lambda x, y: x + y, zip(numbers, c))) + numbers[-1]#вызывается для первых двух элементов,затем для их вычисления и третьего
        if eval(equation):
            print ('YES')
            stop = True
            break
    if stop:
        break
else:
    print ('NO')
