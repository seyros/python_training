In [1]: from datetime import date

In [2]: date?
Init signature: date(self, /, *args, **kwargs)
Docstring:      date(year, month, day) --> date object
File:           ~/miniconda3/lib/python3.5/datetime.py
Type:           type

In [3]: date_in_past = date(2000, 1, 15)

In [4]: date_in_past?
Type:        date
String form: 2000-01-15
File:        ~/miniconda3/lib/python3.5/datetime.py
Docstring:   date(year, month, day) --> date object

In [5]: date_in_past.year
Out[5]: 2000

In [6]: date_in_past.month
Out[6]: 1

In [7]: date_in_past.day
Out[7]: 15

In [8]: date_in_past.weekday
Out[8]: <function date.weekday>

In [9]: date_in_past.weekday()
Out[9]: 5

In [10]: date_in_past = date(1976, 2, 25)

In [11]: date_in_past.weekday()
Out[11]: 2

In [12]: date_in_future = date(2020,1,15)

In [13]: date_in_past < date_in_future
Out[13]: True

In [14]: delta = date_in_future - date_in_past

In [15]: delta
Out[15]: datetime.timedelta(16030)

In [16]: delta?
Type:        timedelta
String form: 16030 days, 0:00:00
File:        ~/miniconda3/lib/python3.5/datetime.py
Docstring:   Difference between two datetime values.

In [17]: date.today()
Out[17]: datetime.date(2017, 4, 24)

