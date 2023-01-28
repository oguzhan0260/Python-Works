""" Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın 
ve şu kurallara göre ekrana şu yazıları yazdırın.

 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez
 """

print("Beden kitle index hesaplayıcıya hoşgeldiniz.")

boy= float(input("Boy:"))
kilo= float(input("Kilo:"))

index= kilo / boy**2
if index< 18.5:
    print("-----------\nZayıfsınız\n","idex'iniz:",index)

elif index>= 18.5 and index<25:
    print("-----------\nNormalsiniz\n","idex'iniz:",index)
elif index>=25 and index<30:
    print("-----------\nFazla Kilolusunuz\n","idex'iniz:",index)
elif index>30:
    print("-----------\nObezsiniz\n","idex'iniz:",index)
