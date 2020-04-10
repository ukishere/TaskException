# class PolishNotation():
#     def __init__(self, x, y):
#         self.x = int(x)
#         self.y = int(y)
#
#     def __pos__(self):
#         return self.x + self.y
#
#     def __neg__(self):
#         return self.x - self.y
#
#     def __mul__(self, other):
#         return self.x * self.y
#
#     def __truediv__(self, other):
#         return self.x / self.y
#
# def calculation(current_words):
#     operands = PolishNotation(current_words[1], current_words[2])
#     result = 0
#
#     if current_words[0] == '+':
#         result = +operands
#     if current_words[0] == '-':
#         result = -operands
#     if current_words[0] == '*':
#         result = operands * 0
#     try:
#         if current_words[0] == '/':
#             result = operands / 0
#     except ZeroDivisionError:
#         print('Нельзя делить на ноль')
#         return None
#     return(result)

def calculation(current_words):

    if current_words[0] == '+':
        result = current_words[1] + current_words[2]
        return result
    if current_words[0] == '-':
        result = current_words[1] - current_words[2]
        return result
    if current_words[0] == '*':
        result = current_words[1] * current_words[2]
        return result
    try:
        if current_words[0] == '/':
            result = current_words[1] / current_words[2]
    except ZeroDivisionError:
        print('Нельзя делить на ноль')
        return None
    else:
        return result

    return None

string = input('Введите выражение: ')

list_of_operations = ['+', '-',  '*', '/']
current_words = string.split()

assert len(current_words[0]) == 1 and current_words[0] in list_of_operations, \
    'Первым символом должна быть только одна из операцийй (+, -, *, /) отделенная от чисел пробелом'
#assert current_words[0] in list_of_operands, 'В польской нотации первой должна стоять операция'
assert len(current_words) == 3, 'Программа работает только с двумя числами'
try:
    current_words[1] = int(current_words[1])
    current_words[2] = int(current_words[2])
except ValueError:
    print('Переменные должны быть числами')
else:
    assert current_words[1] >= 0 and current_words[2] >= 0, 'Числа должны быть положительными'

    result = calculation(current_words)
    if result == None:
        pass
    else:
        print(f'Результат: {result}')

# def verification(current_words):
#     try:
#         assert current_words[0] == '+' or current_words[0] == '-' or current_words[0] == '*' or current_words[0] == '/', ''
#         int(current_words[1])
#         int(current_words[2])
#     except AssertionError:
#         return 'Неверное положение или значение оператора'
#     except ValueError:
#         return 'Неверное значение или положение переменных'
#     else:
#         return 'Проверка прошла успешно'
#
# def calculation_search(all_words):
#     count = 0
#     status = ''
#     while count <= len(all_words)-3:
#         current_words = [all_words[count], all_words[count+1], all_words[count+2]]
#         current_words.reverse()
#         status = verification(current_words)
#         if status == 'Проверка прошла успешно': return count
#         else: count += 1
#
#     return None
#
# def step_by_step_calculation(all_words):
#     if len(all_words) >= 3:
#         while len(all_words) > 1:
#             if calculation_search(all_words) != None:
#                 count = calculation_search(all_words)
#                 current_words = [all_words[count], all_words[count+1], all_words[count+2]]
#                 current_words.reverse()
#                 if calculation(current_words) == None: return None
#                 else:
#                     all_words[count] = calculation(current_words)
#                     all_words.pop(count+1)
#                     all_words.pop(count+1)
#             else:
#                 print('Неверное количество переменных')
#                 return None
#         return all_words
#     else:
#         print('Неверный ввод. Необходимо не менее трех символов')
#         return None
#
# while True:
#
#     string = input('Введите выражение или нажмите q для выхода: ')
#     if string == 'q': break
#
#     all_words = string.split()
#     all_words.reverse()
#
#     if step_by_step_calculation(all_words) != None: print(f'Результат: {all_words[0]}')