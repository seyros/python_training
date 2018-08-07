
import calendar
import random


class Calendar:
    """  return day e.g. 31"""
    def get_day(self):
        d = random.randint(1, 31)
        return d
        pass
    """ return month e.g. 3 """
    def get_month(self):
        m = random.randint(1, 12)
        return m
        pass
    """ return year e.g. 1988 """
    def get_year(self):
        y = random.randint(1900, 2100)
        return y
        pass

# Получаю экземпляр класса, используя методы, получаю день, месяц и год
print("Генерируется дата григорианского календаря в диапазоне от 1900 до 2100 года\n")
test_date = Calendar()
day = test_date.get_day()
month = test_date.get_month()
year = test_date.get_year()

date = "Полученная дата: {}.{}.{}".format(day, month, year)
# ассерты на наличие данных
assert day and month and year, 'Ожидается наличие дня, месяца и года в полученной дате'
# ассерты на тип полученных данных
assert type(day) == int
assert type(month) == int
assert type(year) == int


# проверяю полученную дату на валидность
def is_date_valid(day, month, year):
    valid = True
    if year < 0 or month < 0 or day < 0:
        print('{} невалидна, так как в дате недопустимы отрицательные значения'.format(date))
        valid = False
    if year not in range(1900, 2100):
        print('{} невалидна, так как выходит за пределы диапазона 1900 - 2100 гг'.format(date))
        valid = False
    else:
        if month not in range(1, 12):
            print('{} невалидна, так как в году 12 месяцев'.format(date, d=day, m=month, y=year))
            valid = False
        else:
            days_in_month = calendar.monthrange(year, month)[1]
            if days_in_month == 31:
                _days = 'день'
            else:
                _days = 'дней'
            if day not in range (1, days_in_month):
                print('{} невалидна, так как в {m} месяце {y} года всего {dim} {dd}'
                      .format(date, d=day, m=month, y=year, dim=days_in_month, dd=_days))
                valid = False
    return valid


if is_date_valid(day, month, year):
    print('{} валидна'.format(date))



# """ Второй вариант, упрощённый:
# используется метод date из datetime. При попытке получить обьект типа date из невалидных данных
# будет получена ошибка вида:
# если невалиден день: ValueError: day is out of range for month
# если невалиден месяц:  ValueError: month must be in 1..12
# если невалиден год: ValueError: year is out of range """
#
#
# from datetime import date
# full_date = date(year, month, day)
# print("\nПолученная дата: {}".format(full_date))

