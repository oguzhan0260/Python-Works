""" Problem 4
Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.

Örnek: 97 ---------> Doksan Yedi"""


onlar_basamak=["","On","Yirmi","Otuz","Kırk","Elli","Atmış","Yetmiş","Seksen","Doksan"]
birler_basamak=["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
def okunus (say):
    onlar_sayısı= say//10
    birler_sayısı= say%10

    
    return onlar_basamak[onlar_sayısı]+" "+ birler_basamak[birler_sayısı]


say= int(input("Sayı:"))
print(okunus(say))