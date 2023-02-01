"""
Problem 3
1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.

*İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.*"""


for i in range(10):
    for j in range(10):
        print("{} x {} = {}".format(i,j,i*j))