"""Problem 1
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. 
Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)"""



say=int(input("Sayı:"))
toplam=0

tam_bölenler=[i for i in range(1,say) if say %i ==0]

for i in tam_bölenler:
    toplam+=i
if toplam==say:
    print(say, "MÜKEMMEL SAYIDIR","\nTam Bölenleri",tam_bölenler)
else:
    print(say, "MÜKEMMEL SAYI DEĞİL","\nTam Bölenleri",tam_bölenler,"\nToplam",toplam)





