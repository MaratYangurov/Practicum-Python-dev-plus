import datetime as dt
def accept_package(package_data): #это точка входа в программу, функция, которая вызывается первой; на вход она принимает пакет с данными.
    # Здесь добавляем данные из package_data в storage_data
    storage_data = {}
    for time, steps in package_data:
        storage_data[time] = steps
    return storage_data

def check_correct_data(package_data): #функция проверяющая корректность полученного пакета.
    if not package_data:
        return False
    elif not accept_package(package).items():
        return False
    else:
        return True


weight = 75 #Вес конст

height = 175 #Рост

K_1 = 0.035

K_2 = 0.029

len_step_m = 0.65 #Длина шага м.

transfer_coeff = 1000 #Перевод длины и м. в км.

def get_step_day(steps): #функция должна вернуть общее количество шагов за текущие сутки.
    sum_steps = 0
    for time, steps in accept_package(package).items():
        sum_steps +=steps
    return sum_steps

def get_distance(steps): #пересчитайте шаги в километры. Это арифметика, серьёзное дело. Функция должна вернуть дистанцию в километрах.
    dist = (get_step_day(steps) * len_step_m) / transfer_coeff
    return dist

def get_times(current_time): #Проверка корректности параметра времени
    max_times = dt.time(0, 0, 0)
    for times in accept_package(package).keys():
        best_times = dt.time(hour=int(times.split(':')[0]), minute=int(times.split(':')[1]), second=int(times.split(':')[-1]))
        if max_times < best_times:
            max_times = best_times
    return max_times

def get_spent_calories(dist, current_time): #должна вычислять и возвращать количество килокалорий, истраченных за текущие сутки. Этот расчёт вы уже выполняли, перенесите свой код в эту функцию.
    hours = dt.time.strftime(current_time, '%H')
    minutes = dt.time.strftime(current_time, '%M')
    seconds = dt.time.strftime(current_time, '%S')

    total_minutes = int(hours) * 60 + int(minutes) + int(seconds) / 60 #Расчет общего времени
    # Предполагая, что у вас есть функции get_distance
    mean_speed = get_distance(value) / total_minutes #Расчет скорости
    spend_calories = ((0.035 * weight) + ((mean_speed ** 2) / height) * (0.029 * weight)) * total_minutes #Расчет расходуемых каллорий
    return spend_calories
def get_achievement(dist):
    if get_distance(value) >= 6.5:
        achievement = 'Отличный результат! Цель достигнута.'
    elif get_distance(value) >= 3.9:
        achievement = 'Неплохо! День был продуктивным.'
    elif get_distance(value) >= 2:
        achievement = 'Маловато, но завтра наверстаем!'
    else:
        achievement = 'Лежать тоже полезно. Главное - участие, а не победа!'
    return achievement

package = [
    ('9:36:02', 3500), #время / шаги
    ('11:36:02', 20000),
    ('7:36:02', 10000)
]

for key, value in accept_package(package).items():
    output = f'Время: {get_times(key)} Количество шагов за сегодня: {get_step_day(value)} шагов. Дистанция составила {get_distance(value):.2f} км. Вы сожгли {get_spent_calories(get_distance(value), get_times(key)):.2f} ккал. {get_achievement(value)}'

print(output)