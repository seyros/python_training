from datetime import date
import random
# import calendar

print("Введите дату григорианского календаря:\n")


# class Calendar:
#     """  return day e.g. 31"""
#     def get_day(self):
#         d = random.randint(1, 31)
#         print("День месяца: {}".format(d))
#         return d
#         pass
#     """ return month e.g. 3 """
#     def get_month(self):
#         m = random.randint(1, 12)
#         print("Месяц: {}".format(m))
#         return m
#         pass
#     """ return year e.g. 1988 """
#     def get_year(self):
#         y = random.randint(1900, 2099)
#         print("Год: {}".format(y))
#         return y
#         pass
#
#
# test_case = Calendar()
# print(test_case.get_day())
# print(test_case.get_month())
# print(test_case.get_year())
# full_date = date(test_case.get_year(), test_case.get_month(), test_case.get_day())
#
# print("\nПолная дата: {}".format(full_date))
# print(type(full_date))
# # calendar.monthrange(2011, 2)
# a = calendar.itermonthdays(2018, 8)
# a = calendar.monthcalendar
# print(a)
import calendar
a = calendar.LocaleHTMLCalendar(locale='Russian_Russia')
with open('calendar.html', 'w') as g:
    print(a.formatyear(2014, width=4), file=g)