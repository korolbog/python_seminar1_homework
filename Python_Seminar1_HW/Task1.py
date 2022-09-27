# Задача 1. Напишите программу,
# которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
n = int(input('Введите номер дня недели: '))
if 0 < n < 6:
    print(f'- {weekdays[n-1]} - выходной?\n- Нет.')
elif 5 < n < 8:
    print(f'- {weekdays[n-1]} - выходной?\n- Да!')
else:
    print('Вы ввели неправильный номер')