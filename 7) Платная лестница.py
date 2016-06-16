print('Введите цены ступеней(через запятую)')
a = input();
print('Введите ширину шага')
s = int(input())
b = [int(i) for i in a.split(',')]
if s == 0:
    s = 1;

if s > len(b):
    print (b[len(b)-1])
else:
    cost = (b[:s]);
    for i in range(s,len(b)):
        cost.append(b[i] + min([cost[i-j-1] for j in range(s)]))  #вставляет значение в список
    print (cost[len(cost)-1])
