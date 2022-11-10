import telebot
import loger as log
import rational_checker as rc

bot = telebot.TeleBot('')


def round_(number1, number2):  # Определение количества знаков после точки
    if '.' in number1:
        round1 = len(number1[number1.index('.') + 1:])
    else:
        round1 = 0
    if '.' in number2:
        round2 = len(number2[number2.index('.') + 1:])
    else:
        round2 = 0
    if round1 > round2:
        round_max = round1
    else:
        round_max = round2
    return round_max


@bot.message_handler(commands=['start'])
def start(message):
    log.loger(f'Пользователь {message.from_user.first_name} добавил твоего бота')
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}, я простейший бот калькулятор, написанный'
                                      f' Артемом Приваловым.')
    with open("greetings.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id, 'Просто напиши /calculate, если я тебе понадоблюсь')


@bot.message_handler(commands=['calculate'])
def calculate(message):
    log.loger(f'Пользователь {message.from_user.first_name} начал пользоваться калькулятором')
    bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
    bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                      '2. Работа с комплексными числами\n'
                                      '3. Выход из приложения')
    bot.register_next_step_handler(callback=change, message=message)


def change(message):
    if message.text.strip() == '1':
        bot.send_message(message.chat.id, 'Вы выбрали работу с рациональными числами')
        log.loger(f'Пользователь {message.from_user.first_name} выбрал режим работы с рациональными числами')
        bot.send_message(message.chat.id, 'Какую операцию вы хотите произвести с числами: ')
        bot.send_message(message.chat.id, '1. Сложение\n'
                                          '2. Вычитание\n'
                                          '3. Умножение\n'
                                          '4. Деление')
        bot.register_next_step_handler(callback=rational_actions, message=message)
    elif message.text.strip() == '2':
        bot.send_message(message.chat.id, 'Вы выбрали работу с комплексными числами')
        log.loger(f'Пользователь {message.from_user.first_name} выбрал режим работы с комплексными числами')
        bot.send_message(message.chat.id, 'Какую операцию вы хотите произвести с числами: ')
        bot.send_message(message.chat.id, '1. Сложение\n'
                                          '2. Вычитание\n'
                                          '3. Умножение\n'
                                          '4. Деление')
        bot.register_next_step_handler(callback=complex_actions, message=message)
    elif message.text.strip() == '3':
        log.loger(f'Пользователь {message.from_user.first_name} завершил работу приложения')
        bot.send_message(message.chat.id, 'Работа приложения завершена. Наберите /calculate, если понадоблюсь вновь.')
    elif message.text.strip() == '/calculate':
        log.loger(f'Пользователь {message.from_user.first_name} прервал прошлую операцию, и вызвал функцию '
                  f'калькулятора')
        bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
        bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                          '2. Работа с комплексными числами\n'
                                          '3. Выход из приложения')
        bot.register_next_step_handler(callback=change, message=message)
    elif message.text.strip() == '/start':
        log.loger(f'Пользователь {message.from_user.first_name} прервал прошлую операцию, и вызвал функцию '
                  f'СТАРТ')
        bot.send_message(message.chat.id,
                         f'Привет {message.from_user.first_name}, я простейший бот калькулятор, написанный'
                         f' Артемом Приваловым.')
        with open("greetings.jpg", "rb") as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Просто напиши /calculate, если я тебе понадоблюсь')
    else:
        log.loger(f'Пользователь {message.from_user.first_name} ввел {message.text} при попытке режима работы')
        bot.send_message(message.chat.id, 'Такого пункта меню нет')
        bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
        bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                          '2. Работа с комплексными числами\n'
                                          '3. Выход из приложения')
        bot.register_next_step_handler(callback=change, message=message)


def rational_actions(message):
    if message.text.strip() == '1':
        log.loger(f'Пользователь {message.from_user.first_name} выбрал операцию сложения')
        bot.send_message(message.chat.id, 'Введите два рациональных числа через пробел, а я их сложу')
        bot.register_next_step_handler(callback=summator, message=message)
    elif message.text.strip() == '2':
        log.loger(f'Пользователь {message.from_user.first_name} выбрал операцию вычитания')
        bot.send_message(message.chat.id, 'Введите два рациональных числа через пробел, а я вычту из первого второе')
        bot.register_next_step_handler(callback=subtraction, message=message)
    elif message.text.strip() == '3':
        log.loger(f'Пользователь {message.from_user.first_name} выбрал операцию умножения')
        bot.send_message(message.chat.id, 'Введите два рациональных числа через пробел, а я их перемножу')
        bot.register_next_step_handler(callback=multiplication, message=message)
    elif message.text.strip() == '4':
        log.loger(f'Пользователь {message.from_user.first_name} выбрал операцию деления')
        bot.send_message(message.chat.id, 'Введите два рациональных числа через пробел, а я поделю первое на второе')
        bot.register_next_step_handler(callback=division, message=message)
    elif message.text.strip() == '/calculate':
        log.loger(f'Пользователь {message.from_user.first_name} прервал прошлую операцию, и вызвал функцию '
                  f'калькулятора')
        bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
        bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                          '2. Работа с комплексными числами\n'
                                          '3. Выход из приложения')
        bot.register_next_step_handler(callback=change, message=message)
    elif message.text.strip() == '/start':
        log.loger(f'Пользователь {message.from_user.first_name} прервал прошлую операцию, и вызвал функцию '
                  f'СТАРТ')
        bot.send_message(message.chat.id,
                         f'Привет {message.from_user.first_name}, я простейший бот калькулятор, написанный'
                         f' Артемом Приваловым.')
        with open("greetings.jpg", "rb") as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Просто напиши /calculate, если я тебе понадоблюсь')
    else:
        bot.send_message(message.chat.id, 'Такого пункта меню нет')
        bot.send_message(message.chat.id, 'Какую операцию вы хотите произвести с числами: ')
        bot.send_message(message.chat.id, '1. Сложение\n'
                                          '2. Вычитание\n'
                                          '3. Умножение\n'
                                          '4. Деление')
        bot.register_next_step_handler(callback=rational_actions, message=message)


def summator(message):
    lst = message.text.replace(',', '.').split()
    if len(lst) == 2 and rc.checker(lst[0]) and rc.checker(lst[1]):
        result = round(float(lst[0]) + float(lst[1]), round_(lst[0], lst[1]))
        if result % 1 == 0:
            result = int(result)
        bot.send_message(message.chat.id,
                         f'Ответ: {result}')
        log.loger(f'Пользователь {message.from_user.first_name} ввел числа {lst[0]} и {lst[1]}')
        log.loger(f'Ответ для {message.from_user.first_name}: {result}')
        bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
        bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                          '2. Работа с комплексными числами\n'
                                          '3. Выход из приложения')
        bot.register_next_step_handler(callback=change, message=message)
    elif message.text.strip() == '/calculate':
        log.loger(f'Пользователь {message.from_user.first_name} прервал прошлую операцию, и вызвал функцию '
                  f'калькулятора')
        bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
        bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                          '2. Работа с комплексными числами\n'
                                          '3. Выход из приложения')
        bot.register_next_step_handler(callback=change, message=message)
    elif message.text.strip() == '/start':
        log.loger(f'Пользователь {message.from_user.first_name} прервал прошлую операцию, и вызвал функцию '
                  f'СТАРТ')
        bot.send_message(message.chat.id,
                         f'Привет {message.from_user.first_name}, я простейший бот калькулятор, написанный'
                         f' Артемом Приваловым.')
        with open("greetings.jpg", "rb") as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Просто напиши /calculate, если я тебе понадоблюсь')
    else:
        bot.send_message(message.chat.id, 'Вы ввели неверные данные')
        bot.send_message(message.chat.id, 'Введите два рациональных числа через пробел, а я их сложу')
        bot.register_next_step_handler(callback=summator, message=message)


def subtraction(message):
    lst = message.text.replace(',', '.').split()
    if len(lst) == 2 and rc.checker(lst[0]) and rc.checker(lst[1]):
        result = round(float(lst[0]) - float(lst[1]), round_(lst[0], lst[1]))
        if result % 1 == 0:
            result = int(result)
        bot.send_message(message.chat.id,
                         f'Ответ: {result}')
        log.loger(f'Пользователь {message.from_user.first_name} ввел числа {lst[0]} и {lst[1]}')
        log.loger(f'Ответ для {message.from_user.first_name}: {result}')
        bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
        bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                          '2. Работа с комплексными числами\n'
                                          '3. Выход из приложения')
        bot.register_next_step_handler(callback=change, message=message)
    elif message.text.strip() == '/calculate':
        log.loger(f'Пользователь {message.from_user.first_name} прервал прошлую операцию, и вызвал функцию '
                  f'калькулятора')
        bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
        bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                          '2. Работа с комплексными числами\n'
                                          '3. Выход из приложения')
        bot.register_next_step_handler(callback=change, message=message)
    elif message.text.strip() == '/start':
        log.loger(f'Пользователь {message.from_user.first_name} прервал прошлую операцию, и вызвал функцию '
                  f'СТАРТ')
        bot.send_message(message.chat.id,
                         f'Привет {message.from_user.first_name}, я простейший бот калькулятор, написанный'
                         f' Артемом Приваловым.')
        with open("greetings.jpg", "rb") as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Просто напиши /calculate, если я тебе понадоблюсь')
    else:
        bot.send_message(message.chat.id, 'Вы ввели неверные данные')
        bot.send_message(message.chat.id, 'Введите два рациональных числа через пробел, а я вычту из первого второе')
        bot.register_next_step_handler(callback=subtraction, message=message)


def multiplication(message):
    lst = message.text.replace(',', '.').split()
    if len(lst) == 2 and rc.checker(lst[0]) and rc.checker(lst[1]):
        result = round(float(lst[0]) * float(lst[1]), round_(lst[0], lst[1]))
        if result % 1 == 0:
            result = int(result)
        bot.send_message(message.chat.id,
                         f'Ответ: {result}')
        log.loger(f'Пользователь {message.from_user.first_name} ввел числа {lst[0]} и {lst[1]}')
        log.loger(f'Ответ для {message.from_user.first_name}: {result}')
        bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
        bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                          '2. Работа с комплексными числами\n'
                                          '3. Выход из приложения')
        bot.register_next_step_handler(callback=change, message=message)
    elif message.text.strip() == '/calculate':
        log.loger(f'Пользователь {message.from_user.first_name} прервал прошлую операцию, и вызвал функцию '
                  f'калькулятора')
        bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
        bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                          '2. Работа с комплексными числами\n'
                                          '3. Выход из приложения')
        bot.register_next_step_handler(callback=change, message=message)
    elif message.text.strip() == '/start':
        log.loger(f'Пользователь {message.from_user.first_name} прервал прошлую операцию, и вызвал функцию '
                  f'СТАРТ')
        bot.send_message(message.chat.id,
                         f'Привет {message.from_user.first_name}, я простейший бот калькулятор, написанный'
                         f' Артемом Приваловым.')
        with open("greetings.jpg", "rb") as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Просто напиши /calculate, если я тебе понадоблюсь')
    else:
        bot.send_message(message.chat.id, 'Вы ввели неверные данные')
        bot.send_message(message.chat.id, 'Введите два рациональных числа через пробел, а я их перемножу')
        bot.register_next_step_handler(callback=multiplication, message=message)


def division(message):
    lst = message.text.replace(',', '.').split()
    if len(lst) == 2 and rc.checker(lst[0]) and rc.checker(lst[1]):
        if lst[1] != '0':
            result = float(lst[0]) / float(lst[1])
            if result % 1 == 0:
                result = int(result)
            bot.send_message(message.chat.id,
                             f'Ответ: {result}')
            log.loger(f'Пользователь {message.from_user.first_name} ввел числа {lst[0]} и {lst[1]}')
            log.loger(f'Ответ для {message.from_user.first_name}: {result}')
            bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
            bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                              '2. Работа с комплексными числами\n'
                                              '3. Выход из приложения')
            bot.register_next_step_handler(callback=change, message=message)
        else:
            log.loger(f'Пользователь {message.from_user.first_name} пытался разделить на ноль')
            bot.send_message(message.chat.id, 'Братишь, на ноль делить нельзя')
            bot.send_message(message.chat.id, 'Введите два рациональных числа через пробел, '
                                              'а я поделю первое на второе')
            bot.register_next_step_handler(callback=division, message=message)
    elif message.text.strip() == '/calculate':
        log.loger(f'Пользователь {message.from_user.first_name} прервал прошлую операцию, и вызвал функцию '
                  f'калькулятора')
        bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
        bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                          '2. Работа с комплексными числами\n'
                                          '3. Выход из приложения')
        bot.register_next_step_handler(callback=change, message=message)
    elif message.text.strip() == '/start':
        log.loger(f'Пользователь {message.from_user.first_name} прервал прошлую операцию, и вызвал функцию '
                  f'СТАРТ')
        bot.send_message(message.chat.id,
                         f'Привет {message.from_user.first_name}, я простейший бот калькулятор, написанный'
                         f' Артемом Приваловым.')
        with open("greetings.jpg", "rb") as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Просто напиши /calculate, если я тебе понадоблюсь')
    else:
        bot.send_message(message.chat.id, 'Вы ввели неверные данные')
        bot.send_message(message.chat.id, 'Введите два рациональных числа через пробел, а я поделю первое на второе')
        bot.register_next_step_handler(callback=division, message=message)


def complex_actions(message):
    if message.text.strip() == '1':
        log.loger(f'Пользователь {message.from_user.first_name} выбрал операцию сложения')
        bot.send_message(message.chat.id, 'Первое комплексное число имеет вид a+bi, а второе x+yi')
        bot.send_message(message.chat.id, 'Введите через пробел a, b, x и y, '
                                          'а я вычислю сумму получившихся комплексных чисел')
        bot.register_next_step_handler(callback=comp_summator, message=message)
    elif message.text.strip() == '2':
        log.loger(f'Пользователь {message.from_user.first_name} выбрал операцию вычитания')
        bot.send_message(message.chat.id, 'Первое комплексное число имеет вид a+bi, а второе x+yi')
        bot.send_message(message.chat.id, 'Введите через пробел a, b, x и y, '
                                          'а я вычислю разность получившихся комплексных чисел')
        bot.register_next_step_handler(callback=comp_subtraction, message=message)
    elif message.text.strip() == '3':
        log.loger(f'Пользователь {message.from_user.first_name} выбрал операцию умножения')
        bot.send_message(message.chat.id, 'Первое комплексное число имеет вид a+bi, а второе x+yi')
        bot.send_message(message.chat.id, 'Введите через пробел a, b, x и y, '
                                          'а я вычислю произведение получившихся комплексных чисел')
        bot.register_next_step_handler(callback=comp_mult, message=message)
    elif message.text.strip() == '4':
        log.loger(f'Пользователь {message.from_user.first_name} выбрал операцию деления')
        bot.send_message(message.chat.id, 'Первое комплексное число имеет вид a+bi, а второе x+yi')
        bot.send_message(message.chat.id, 'Введите через пробел a, b, x и y, '
                                          'а я вычислю частное получившихся комплексных чисел')
        bot.register_next_step_handler(callback=comp_div, message=message)
    elif message.text.strip() == '/calculate':
        log.loger(f'Пользователь {message.from_user.first_name} прервал прошлую операцию, и вызвал функцию '
                  f'калькулятора')
        bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
        bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                          '2. Работа с комплексными числами\n'
                                          '3. Выход из приложения')
        bot.register_next_step_handler(callback=change, message=message)
    elif message.text.strip() == '/start':
        log.loger(f'Пользователь {message.from_user.first_name} прервал прошлую операцию, и вызвал функцию '
                  f'СТАРТ')
        bot.send_message(message.chat.id,
                         f'Привет {message.from_user.first_name}, я простейший бот калькулятор, написанный'
                         f' Артемом Приваловым.')
        with open("greetings.jpg", "rb") as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Просто напиши /calculate, если я тебе понадоблюсь')
    else:
        bot.send_message(message.chat.id, 'Такого пункта меню нет')
        bot.send_message(message.chat.id, 'Какую операцию вы хотите произвести с числами: ')
        bot.send_message(message.chat.id, '1. Сложение\n'
                                          '2. Вычитание')
        bot.register_next_step_handler(callback=complex_actions, message=message)


def comp_summator(message):
    lst = message.text.replace(',', '.').split()
    if len(lst) == 4 and rc.checker(lst[0]) and rc.checker(lst[1]) and rc.checker(lst[2]) and rc.checker(lst[3]):
        log.loger(f'Пользователь {message.from_user.first_name} ввел числа {lst[0]}, {lst[1]}, {lst[2]}, {lst[3]}')
        number1 = round(float(lst[0]) + float(lst[2]), round_(lst[0], lst[2]))
        number2 = round(float(lst[1]) + float(lst[3]), round_(lst[1], lst[3]))
        if number1 % 1 == 0:
            number1 = int(number1)
        if number2 % 1 == 0:
            number2 = int(number2)
        if number1 == 0:
            if number2 == 0:
                log.loger(f'Ответ для {message.from_user.first_name}: 0')
                bot.send_message(message.chat.id,
                                 f'Ответ: 0')
            elif number2 == 1:
                bot.send_message(message.chat.id,
                                 f'Ответ: i')
                log.loger(f'Ответ для {message.from_user.first_name}: i')
            elif number2 == -1:
                bot.send_message(message.chat.id,
                                 f'Ответ: -i')
                log.loger(f'Ответ для {message.from_user.first_name}: -i')
            else:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number2}i')
                log.loger(f'Ответ для {message.from_user.first_name}: {number2}i')
        else:
            if number2 == 0:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number1}')
                log.loger(f'Ответ для {message.from_user.first_name}: {number1}')
            elif number2 == 1:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number1}+i')
                log.loger(f'Ответ для {message.from_user.first_name}: {number1}+i')
            elif number2 == -1:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number1}-i')
                log.loger(f'Ответ для {message.from_user.first_name}: {number1}-i')
            elif number2 < -1 or -1 < number2 < 0:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number1}{number2}i')
                log.loger(f'Ответ для {message.from_user.first_name}: {number1}{number2}i')
            else:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number1}+{number2}i')
                log.loger(f'Ответ для {message.from_user.first_name}: {number1}+{number2}i')
        bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
        bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                          '2. Работа с комплексными числами\n'
                                          '3. Выход из приложения')
        bot.register_next_step_handler(callback=change, message=message)
    elif message.text.strip() == '/calculate':
        log.loger(f'Пользователь {message.from_user.first_name} прервал прошлую операцию, и вызвал функцию '
                  f'калькулятора')
        bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
        bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                          '2. Работа с комплексными числами\n'
                                          '3. Выход из приложения')
        bot.register_next_step_handler(callback=change, message=message)
    elif message.text.strip() == '/start':
        log.loger(f'Пользователь {message.from_user.first_name} прервал прошлую операцию, и вызвал функцию '
                  f'СТАРТ')
        bot.send_message(message.chat.id,
                         f'Привет {message.from_user.first_name}, я простейший бот калькулятор, написанный'
                         f' Артемом Приваловым.')
        with open("greetings.jpg", "rb") as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Просто напиши /calculate, если я тебе понадоблюсь')
    else:
        bot.send_message(message.chat.id, 'Вы ввели неверные данные')
        bot.send_message(message.chat.id, 'Первое комплексное число имеет вид a+bi, а второе x+yi')
        bot.send_message(message.chat.id, 'Введите через пробел значения a, b, x и y, '
                                          'а я вычислю сумму получившихся комплексных чисел')
        bot.register_next_step_handler(callback=comp_summator, message=message)


def comp_subtraction(message):
    lst = message.text.replace(',', '.').split()
    if len(lst) == 4 and rc.checker(lst[0]) and rc.checker(lst[1]) and rc.checker(lst[2]) and rc.checker(lst[3]):
        log.loger(f'Пользователь {message.from_user.first_name} ввел числа {lst[0]}, {lst[1]}, {lst[2]}, {lst[3]}')
        number1 = round(float(lst[0]) - float(lst[2]), round_(lst[0], lst[2]))
        number2 = round(float(lst[1]) - float(lst[3]), round_(lst[1], lst[3]))
        if number1 % 1 == 0:
            number1 = int(number1)
        if number2 % 1 == 0:
            number2 = int(number2)
        if number1 == 0:
            if number2 == 0:
                log.loger(f'Ответ для {message.from_user.first_name}: 0')
                bot.send_message(message.chat.id,
                                 f'Ответ: 0')
            elif number2 == 1:
                bot.send_message(message.chat.id,
                                 f'Ответ: i')
                log.loger(f'Ответ для {message.from_user.first_name}: i')
            elif number2 == -1:
                bot.send_message(message.chat.id,
                                 f'Ответ: -i')
                log.loger(f'Ответ для {message.from_user.first_name}: -i')
            else:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number2}i')
                log.loger(f'Ответ для {message.from_user.first_name}: {number2}i')
        else:
            if number2 == 0:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number1}')
                log.loger(f'Ответ для {message.from_user.first_name}: {number1}')
            elif number2 == 1:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number1}+i')
                log.loger(f'Ответ для {message.from_user.first_name}: {number1}+i')
            elif number2 == -1:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number1}-i')
                log.loger(f'Ответ для {message.from_user.first_name}: {number1}-i')
            elif number2 < -1 or -1 < number2 < 0:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number1}{number2}i')
                log.loger(f'Ответ для {message.from_user.first_name}: {number1}{number2}i')
            else:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number1}+{number2}i')
                log.loger(f'Ответ для {message.from_user.first_name}: {number1}+{number2}i')
        bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
        bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                          '2. Работа с комплексными числами\n'
                                          '3. Выход из приложения')
        bot.register_next_step_handler(callback=change, message=message)
    elif message.text.strip() == '/calculate':
        log.loger(f'Пользователь {message.from_user.first_name} прервал прошлую операцию, и вызвал функцию '
                  f'калькулятора')
        bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
        bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                          '2. Работа с комплексными числами\n'
                                          '3. Выход из приложения')
        bot.register_next_step_handler(callback=change, message=message)
    elif message.text.strip() == '/start':
        log.loger(f'Пользователь {message.from_user.first_name} прервал прошлую операцию, и вызвал функцию '
                  f'СТАРТ')
        bot.send_message(message.chat.id,
                         f'Привет {message.from_user.first_name}, я простейший бот калькулятор, написанный'
                         f' Артемом Приваловым.')
        with open("greetings.jpg", "rb") as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Просто напиши /calculate, если я тебе понадоблюсь')
    else:
        bot.send_message(message.chat.id, 'Вы ввели неверные данные')
        bot.send_message(message.chat.id, 'Первое комплексное число имеет вид a+bi, а второе x+yi')
        bot.send_message(message.chat.id, 'Введите через пробел значения a, b, x и y, '
                                          'а я вычислю разность получившихся комплексных чисел')
        bot.register_next_step_handler(callback=comp_subtraction, message=message)


def comp_mult(message):
    lst = message.text.replace(',', '.').split()
    if len(lst) == 4 and rc.checker(lst[0]) and rc.checker(lst[1]) and rc.checker(lst[2]) and rc.checker(lst[3]):
        log.loger(f'Пользователь {message.from_user.first_name} ввел числа {lst[0]}, {lst[1]}, {lst[2]}, {lst[3]}')
        number1 = float(lst[0]) * float(lst[2])
        number2 = float(lst[1]) * float(lst[3])
        number3 = float(lst[0]) * float(lst[3])
        number4 = float(lst[1]) * float(lst[2])
        number5 = round(number1 - number2, round_(str(number1), str(number2)))
        number6 = round(number3 + number4, round_(str(number3), str(number4)))
        if number5 % 1 == 0:
            number5 = int(number5)
        if number6 % 1 == 0:
            number6 = int(number6)
        if number5 == 0:
            if number6 == 0:
                log.loger(f'Ответ для {message.from_user.first_name}: 0')
                bot.send_message(message.chat.id,
                                 f'Ответ: 0')
            elif number6 == 1:
                bot.send_message(message.chat.id,
                                 f'Ответ: i')
                log.loger(f'Ответ для {message.from_user.first_name}: i')
            elif number6 == -1:
                bot.send_message(message.chat.id,
                                 f'Ответ: -i')
                log.loger(f'Ответ для {message.from_user.first_name}: -i')
            else:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number6}i')
                log.loger(f'Ответ для {message.from_user.first_name}: {number6}i')
        else:
            if number6 == 0:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number5}')
                log.loger(f'Ответ для {message.from_user.first_name}: {number5}')
            elif number6 == 1:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number5}+i')
                log.loger(f'Ответ для {message.from_user.first_name}: {number5}+i')
            elif number6 == -1:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number5}-i')
                log.loger(f'Ответ для {message.from_user.first_name}: {number5}-i')
            elif number6 < -1 or -1 < number6 < 0:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number5}{number6}i')
                log.loger(f'Ответ для {message.from_user.first_name}: {number5}{number6}i')
            else:
                bot.send_message(message.chat.id,
                                 f'Ответ: {number5}+{number6}i')
                log.loger(f'Ответ для {message.from_user.first_name}: {number5}+{number6}i')
        bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
        bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                          '2. Работа с комплексными числами\n'
                                          '3. Выход из приложения')
        bot.register_next_step_handler(callback=change, message=message)
    elif message.text.strip() == '/calculate':
        log.loger(f'Пользователь {message.from_user.first_name} прервал прошлую операцию, и вызвал функцию '
                  f'калькулятора')
        bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
        bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                          '2. Работа с комплексными числами\n'
                                          '3. Выход из приложения')
        bot.register_next_step_handler(callback=change, message=message)
    elif message.text.strip() == '/start':
        log.loger(f'Пользователь {message.from_user.first_name} прервал прошлую операцию, и вызвал функцию '
                  f'СТАРТ')
        bot.send_message(message.chat.id,
                         f'Привет {message.from_user.first_name}, я простейший бот калькулятор, написанный'
                         f' Артемом Приваловым.')
        with open("greetings.jpg", "rb") as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Просто напиши /calculate, если я тебе понадоблюсь')
    else:
        bot.send_message(message.chat.id, 'Вы ввели неверные данные')
        bot.send_message(message.chat.id, 'Первое комплексное число имеет вид a+bi, а второе x+yi')
        bot.send_message(message.chat.id, 'Введите через пробел значения a, b, x и y, '
                                          'а я вычислю произведение получившихся комплексных чисел')
        bot.register_next_step_handler(callback=comp_mult, message=message)


def comp_div(message):
    lst = message.text.replace(',', '.').split()
    if len(lst) == 4 and rc.checker(lst[0]) and rc.checker(lst[1]) and rc.checker(lst[2]) and rc.checker(lst[3]):
        log.loger(f'Пользователь {message.from_user.first_name} ввел числа {lst[0]}, {lst[1]}, {lst[2]}, {lst[3]}')
        number1 = float(lst[0]) * float(lst[2])
        number2 = float(lst[1]) * float(lst[3])
        number3 = float(lst[1]) * float(lst[2])
        number4 = float(lst[0]) * float(lst[3])
        number5 = round(number1 + number2, round_(str(number1), str(number2)))
        number6 = round(number3 - number4, round_(str(number3), str(number4)))
        number7 = float(lst[2]) ** 2
        number8 = float(lst[3]) ** 2
        number9 = round(number7 + number8, round_(str(number7), str(number8)))
        if number9 != 0:
            number10 = number5 / number9
            number11 = number6 / number9
            if number10 % 1 == 0:
                number10 = int(number10)
            if number11 % 1 == 0:
                number11 = int(number11)
            if number10 == 0:
                if number11 == 0:
                    log.loger(f'Ответ для {message.from_user.first_name}: 0')
                    bot.send_message(message.chat.id,
                                     f'Ответ: 0')
                elif number11 == 1:
                    bot.send_message(message.chat.id,
                                     f'Ответ: i')
                    log.loger(f'Ответ для {message.from_user.first_name}: i')
                elif number11 == -1:
                    bot.send_message(message.chat.id,
                                     f'Ответ: -i')
                    log.loger(f'Ответ для {message.from_user.first_name}: -i')
                else:
                    bot.send_message(message.chat.id,
                                     f'Ответ: {number11}i')
                    log.loger(f'Ответ для {message.from_user.first_name}: {number11}i')
            else:
                if number11 == 0:
                    bot.send_message(message.chat.id,
                                     f'Ответ: {number10}')
                    log.loger(f'Ответ для {message.from_user.first_name}: {number10}')
                elif number11 == 1:
                    bot.send_message(message.chat.id,
                                     f'Ответ: {number10}+i')
                    log.loger(f'Ответ для {message.from_user.first_name}: {number10}+i')
                elif number11 == -1:
                    bot.send_message(message.chat.id,
                                     f'Ответ: {number10}-i')
                    log.loger(f'Ответ для {message.from_user.first_name}: {number10}-i')
                elif number11 < -1 or -1 < number11 < 0:
                    bot.send_message(message.chat.id,
                                     f'Ответ: {number10}{number11}i')
                    log.loger(f'Ответ для {message.from_user.first_name}: {number10}{number11}i')
                else:
                    bot.send_message(message.chat.id,
                                     f'Ответ: {number10}+{number11}i')
                    log.loger(f'Ответ для {message.from_user.first_name}: {number10}+{number11}i')
            bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
            bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                              '2. Работа с комплексными числами\n'
                                              '3. Выход из приложения')
            bot.register_next_step_handler(callback=change, message=message)
        else:
            if float(lst[1]) == 0:
                bot.send_message(message.chat.id, 'Так как коэффициенты b и y равны нолям, то получаем простейшее '
                                                  'деление, а на ноль делить нельзя')
                bot.send_message(message.chat.id, 'Первое комплексное число имеет вид a+bi, а второе x+yi')
                bot.send_message(message.chat.id, 'Введите через пробел значения a, b, x и y, '
                                                  'а я вычислю частное получившихся комплексных чисел')
                bot.register_next_step_handler(callback=comp_div, message=message)
            else:
                bot.send_message(message.chat.id,
                                 f'Ответ: {float(lst[0]) / float(lst[1])}')
                log.loger(f'Ответ для {message.from_user.first_name}: {float(lst[0]) / float(lst[1])}')
                bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
                bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                                  '2. Работа с комплексными числами\n'
                                                  '3. Выход из приложения')
                bot.register_next_step_handler(callback=change, message=message)
    elif message.text.strip() == '/calculate':
        log.loger(f'Пользователь {message.from_user.first_name} прервал прошлую операцию, и вызвал функцию '
                  f'калькулятора')
        bot.send_message(message.chat.id, 'Выберите необходимый пункт меню путем ввода числа: ')
        bot.send_message(message.chat.id, '1. Работа с рациональными числами\n'
                                          '2. Работа с комплексными числами\n'
                                          '3. Выход из приложения')
        bot.register_next_step_handler(callback=change, message=message)
    elif message.text.strip() == '/start':
        log.loger(f'Пользователь {message.from_user.first_name} прервал прошлую операцию, и вызвал функцию '
                  f'СТАРТ')
        bot.send_message(message.chat.id,
                         f'Привет {message.from_user.first_name}, я простейший бот калькулятор, написанный'
                         f' Артемом Приваловым.')
        with open("greetings.jpg", "rb") as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Просто напиши /calculate, если я тебе понадоблюсь')
    else:
        bot.send_message(message.chat.id, 'Вы ввели неверные данные')
        bot.send_message(message.chat.id, 'Первое комплексное число имеет вид a+bi, а второе x+yi')
        bot.send_message(message.chat.id, 'Введите через пробел значения a, b, x и y, '
                                          'а я вычислю частное получившихся комплексных чисел')
        bot.register_next_step_handler(callback=comp_div, message=message)


bot.infinity_polling()
