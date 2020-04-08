# Не сразу увидел условие задания, что работать нужно только с двумя целыми числами
# Синтаксис реализован как в примере из википедии (- * / 15 - 7 + 1 1 3 + 2 + 1 1)
# Для двух целых чисел тоже работает :)

class PolishNotation():
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __pos__(self):
        return self.x + self.y

    def __neg__(self):
        return self.x - self.y

    def __mul__(self, other):
        return self.x * self.y

    def __truediv__(self, other):
        return self.x / self.y

def calculation(current_words):
    operands = PolishNotation(current_words[1], current_words[2])
    result = 0

    if current_words[0] == '+': result = +operands
    if current_words[0] == '-': result = -operands
    if current_words[0] == '*': result = operands * 0
    try:
        if current_words[0] == '/': result = operands / 0
    except ZeroDivisionError:
        print('Нельзя делить на ноль')
        return None
    return(result)

def verification(current_words):
    try:
        assert current_words[0] == '+' or current_words[0] == '-' or current_words[0] == '*' or current_words[0] == '/', ''
        int(current_words[1])
        int(current_words[2])
    except AssertionError:
        return 'Неверное положение или значение оператора'
    except ValueError:
        return 'Неверное значение или положение переменных'
    else:
        return 'Проверка прошла успешно'

def calculation_search(all_words):
    count = 0
    status = ''
    while count <= len(all_words)-3:
        current_words = [all_words[count], all_words[count+1], all_words[count+2]]
        current_words.reverse()
        status = verification(current_words)
        if status == 'Проверка прошла успешно': return count
        else: count += 1

    return None

def step_by_step_calculation(all_words):
    if len(all_words) >= 3:
        while len(all_words) > 1:
            if calculation_search(all_words) != None:
                count = calculation_search(all_words)
                current_words = [all_words[count], all_words[count+1], all_words[count+2]]
                current_words.reverse()
                if calculation(current_words) == None: return None
                else:
                    all_words[count] = calculation(current_words)
                    all_words.pop(count+1)
                    all_words.pop(count+1)
            else:
                print('Неверное количество переменных')
                return None
        return all_words
    else:
        print('Неверный ввод. Необходимо не менее трех символов')
        return None

while True:

    string = input('Введите выражение или нажмите q для выхода: ')
    if string == 'q': break

    all_words = string.split()
    all_words.reverse()

    if step_by_step_calculation(all_words) != None: print(f'Результат: {all_words[0]}')