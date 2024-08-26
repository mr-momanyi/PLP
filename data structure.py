Python 3.13.0a4 (tags/v3.13.0a4:9d34f60, Feb 15 2024, 17:00:30) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_list = []
>>> my_list.append(10, 20, 30, 40)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    my_list.append(10, 20, 30, 40)
TypeError: list.append() takes exactly one argument (4 given)
>>> my_list.append(10)
>>> my_list.append(20)
>>> my_list.append(30)
>>> my_list.append(40)
>>> print (my_list)
[10, 20, 30, 40]
>>> my_list.insert(1, 15)
>>> print(my_list)
[10, 15, 20, 30, 40]
>>> my_list.extend([50, 60, 70])
>>> print(my_list)
[10, 15, 20, 30, 40, 50, 60, 70]
>>> my_list.pop()
70
>>> print(my_list)
[10, 15, 20, 30, 40, 50, 60]
>>> my_list.sort()
>>> print(my_list)
[10, 15, 20, 30, 40, 50, 60]
>>> index_30 = my_list.index(30)
>>> print(my_list)
[10, 15, 20, 30, 40, 50, 60]
>>> print(index_30)
3
