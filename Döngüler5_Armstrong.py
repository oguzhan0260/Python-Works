"""
Problem 2
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4.
 kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4"""

say= (input("Sayı:"))
basamak=0
list=[]
armstrong=0

for i in say:
    basamak +=1
    list.append(int(i))

sek=0
for x in list:
    armstrong += list[sek]**basamak
    sek +=1

if int(say)==armstrong:
    print(say,"Armstorng sayısıdır.",armstrong)
else:
    print(say,"Armstorng sayısı değildir.",armstrong)













    

