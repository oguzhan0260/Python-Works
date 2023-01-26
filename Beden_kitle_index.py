"""
Problem 2
Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)
"""
print("*"*12,"Beden Kitle Index Hesaplama","*"*12)

boy= float(input("Boyunuzu Giriniz:"))
kilo= float(input("Kilo Giriniz:"))

print("Beden Kitle Index:{}".format(kilo/ boy**2))