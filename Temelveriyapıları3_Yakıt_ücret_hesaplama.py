"""
Problem 3
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın
 ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.
"""

Kmde_yakılan_yakıt= float(input("Kilometrede yakılan yakıt:"))
gidilen_yol= float(input("Gidilen Yol:"))
yakıt_fiyatı= float(input("Aldığınız yakıtın litre fiyatı:"))

print("Ödemeniz gereken mikar:{}TL".format(Kmde_yakılan_yakıt*gidilen_yol*yakıt_fiyatı))
