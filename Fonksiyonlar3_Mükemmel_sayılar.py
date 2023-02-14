"""Problem 1
1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. 
Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.

Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır.
Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).
"""
def mükemmelsayı(say):
    toplam=0
    tambölenler=[i for i in range(1,say) if say%i==0]
    for i in tambölenler:
        toplam +=i
    if toplam==say:
        return True
    else:
        return False

for i in range(1,1001):
    if mükemmelsayı(i)==1:
        print(i,"Mükemmel sayıdır.")