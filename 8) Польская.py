def calculate(input_string):
    try:
        stack = [] # задаем список
        for operand in input_string.split(): # цикл по входной строке и превращение ее в список с разделителем в ввиде пробела(НА ВЫХОДЕ ЧТО? ПРАВИЛЬНО, СПИСОК, А НЕ СТРОКА)
            if operand not in '+-*/': # если значение не операнд
                stack.append(operand) # добавляем значение в конец списка
            else:#как только найден операнд
                op2 = stack.pop() #удаляем элемент и возвращаем его (тут последний элемент списка)
                op1 = stack.pop()  #-//-
                expression = op1 + operand + op2 # склеиваем строку и операнд который был найден
                result = eval(expression) # интерпритируем склеенную строку как код и получаем результат вычисления
                stack.append(str(result)) # записываем полученное значение в список
            
        result = stack.pop()
        if len(stack) == 0:
            return result
        else:
            raise Exception ('Ошибка')
            
    except Exception as e :
        
        raise Exception ('Ошибка')



input_string = input()
try:
    print (calculate(input_string))
except Exception as e:
    print (e)
