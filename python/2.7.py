# -- coding: utf-8 --
a=int(input("Введите число: "))
if (a%4 == 0 and a%100 != 0) or (a%400 == 0): 
    print("Год високосный")
else:
    print("Год не високосный")
