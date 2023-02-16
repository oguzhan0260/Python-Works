import random
import time
x=random.randint(1,10)
print("""****************************

 Sayı Tahmin OYUNU
 
 1 ile 10 arası sayı tahmin edin

 ************************""")
tahmin_hakkı=3
while True:
    print("-----Kalan Tahmin Hakkınız:",tahmin_hakkı,"-----")

    tahmin=int(input("Tahmininizi Girin:"))
    if tahmin_hakkı==1:
        print("Tahmin Hakkınız Bitti, Kaybettiniz. Dogru sayı :",x)
        break
    elif tahmin!=x :
        tahmin_hakkı -=1
        if tahmin<x:
            time.sleep(2)
            print("Daha yüksek bir sayı söyleyin")
        elif tahmin>x:
            time.sleep(2)
            print("Daha düşük bir sayı söyleyin")
        

    elif tahmin==x and tahmin>0:
        print("Doğru TAHMİN ETTİNİZ! . SAYI",x)
        break
    
    

    
    