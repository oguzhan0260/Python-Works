print("""******************

Gelişmiş Hesap Makinesi
Yapmak istediğiniz işlemin numarsını tuşlayınız.
1-Cos Hesaplama
2-Sin hesaplama
3-Ondalıklı sayıyı Aşşagı yuvalama
4-Ondalıklı sayıyı Yukarı Yuvarlama
5- radians ( Convert angle x from degrees to radians)
6- degrees( Convert angle x from radians to degrees.)

0-Çıkış
""")
import math

while True:
    işlem=int(input("********************\nİşlem Numarası:"))

    if işlem==0:
        print("Çıkış Yapıldı")
        break
        
    elif işlem==1:
        x=int((input("Rad cinsinden Hesaplamak istediğiniz cos degeri:")))
        print(math.cos(x))
    
    elif işlem==2:
        x=int((input("Rad cinsinden Hesaplamak istediğiniz sin degeri:")))
        print(math.sin(x))

    elif işlem==3:
        x=float((input("Aşşagı yuvalamak istediğiniz ondalıklı sayı:")))
        print(math.floor(x))

    elif işlem==4:
        x=float(input("Yukarı yuvalamak istediğiniz ondalıklı sayı:"))
        print(math.ceil(x))
        
    elif işlem==5:
        x=int(input("Radyandan, dereceye çevrilecek.\nÇevirmek istediğiniz radyan değeri:"))
        print(math.radians(x))

    elif işlem==6:
        x=int(input("Dereceden radyana çevrilecek.\nÇevirmek istediğiniz derce değeri:"))
        print(math.degrees(x))
        
    else:
        print("Geçersiz işlem no su girdiniz. Tekar deneyiniz...")