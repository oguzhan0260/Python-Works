""" 2. dereceden bir bilinmeyenli denklemin köklerini bulma
Denklem : ax^2 + bx + c
Deltayı Hesaplama:  b ** 2 -  4 * a * c
Birinci Kök : (-b - delta ** 0.5) / (2*a)
İkinci Kök : (-b + delta ** 0.5) / (2*a) """

print("*"*15,"2. dereceden bir bilinmeyenli denklemin köklerini bulma simülatörü","*"*15)

a=int(input("a degerini giriniz:"))
b=int(input("b degerini giriniz:"))
c=int(input("c degerini giriniz:"))

delta= b**2 - 4 *a*c
print("Birinci Kök= {:.2}\nİkinci Kök: {:.2}".format((-b - delta ** 0.5) / (2*a),(-b + delta ** 0.5) / (2*a)))

