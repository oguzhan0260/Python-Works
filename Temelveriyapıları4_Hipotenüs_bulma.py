"""
Problem 6
Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.

Hipotenüs Formülü: a^2 + b^2 = c^2
"""
a= int(input("Birinci Kenar uzunluğu:"))
b= int(input("İkinci Kenar uzunluğu:"))


print("Hipotenüs Değeri:{}".format((a**2 + b**2)**0.5))
