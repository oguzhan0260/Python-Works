"""
Örneğin , siz ATM makinesine gidip kartınızı yerleştiriyorsunuz ve program başlıyor...
 Para Çekme, Para Yatırma , Vergileri Ödeme gibi işlemleri tekrar tekrar gerçekleştiriyorsunuz. 
 Programın sona ermesi ise Kart İade seçeneği ile gerçekleşiyor. Yani siz Kart İade tuşuna basmadığınız sürece ATM makinesi
  çalışmaya devam ediyor. Buna bakarak ,aslında ATM makinesi döngü yapılarını kullanıyor diyebiliriz.
"""

kart=True
vergi_miktarı=100
para=500
while kart:
    işlem= int(input("""*******************************************************
1-Para Çek\n2-Para Yatır\n3-Vergi Öde\n0-Çıkış\nGerçekleştirmek istediğiniz işemi tuşlayınız."""))
    if işlem ==0:
        print("İşlem sonlandırıldı. Kartınızı almayı unutmayınız...")
        break
    elif işlem==1:
        print("Mevcut paranız:",para)
        çekilecek_para= int(input("Çıkmak için 0'a basınız\nÇekmek istediğiniz miktarı giriniz:"))
        if para-çekilecek_para <0:
            print("Yetersiz bakiye.İşlem gerçekleştirilemedi.")
        else:
            print("Paranız Çekiliyor... Lütfen para haznesini kontrol ediniz...")
            para -= çekilecek_para
            print("Yeni mevcut bakiyeniz:",para)

    
    elif işlem==2:
        a=0
        print("Mevcut Paranız:",para)
        yatırım_miktar= int(input(" Yatırmak istediğiniz miktarı giriniz:"))
        para += yatırım_miktar
        print("***********Paranız yatırıldı. Yeni mevcut bakiyeniz:",para)

    elif işlem==3:
        
        print("Güncel vergi miktarı:100TL")
        para-= vergi_miktarı
        print("Verginiz Yatırıldı.\nMevcut bakiyeniz:",para)

    elif işlem >3 :
        print("********Geçersiz işlem girdiniz. Lüfen tekrar deneyin.*********")
    
