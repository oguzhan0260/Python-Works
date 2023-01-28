print("Oyuncu Kaydetme Sistemine Hoşgeldiniz")
ad=input("Oyunucunun Adı ve Soyadı:")
takım=input("Oyuncunun Takımı:")
yas=int(input("Oyuncunun Yaşı:"))

bilgiler=[ad,takım, yas]

print("Bilgiler Kaydediliyor...\n{}Bilgiler{}".format("-"*20,"-"*20))

print("Oyuncunu adı: {}\nOyuncunun Takımı:{}\nOyuncunun Yaşı:{}\nBilgiler Kaydedildi.....".format(bilgiler[0],bilgiler[1],bilgiler[2]))
