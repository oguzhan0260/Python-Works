""" Problem 3
Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.

Problem için şu siteye bakabilirsiniz;

http://www.matematikciler.com/6-sinif/matematik-konu-anlatimlari/1020-en-kucuk-ortak-kat-ve-en-buyuk-ortak-bolen-ebob-ekok"""

def ekok(x,y):
    i=0
    while True:
        i+=1
        if i%x==0 and i%y==0:
            return i
            break


x=int(input("Sayı1 :"))
y=int(input("Sayı2 :"))

print("Ekok :",ekok(x,y))