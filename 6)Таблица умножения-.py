def multiply(m,n):
    result_attend = len(str(m * n));
    m_attend = len(str(m));
    n_attend = len(str(n));
    for i in range(1,n+1):
        result = '';
        result += repr(i*m).rjust(result_attend); #расширяем строку,дополняя слева 
        result += '_=_';
        result += repr(i).rjust(n_attend);
        result += '_*_';
        result += repr(m).rjust(m_attend);
        result = result.replace(' ','_',len(result));
        print (result);
print('Введите числа(через запятую)')
vvod = input().split(',')
m=int(vvod[0])
n=int(vvod[1])
multiply(m,n);
