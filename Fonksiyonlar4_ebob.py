"""Problem 2
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.

Problem için şu siteye bakabilirsiniz;

http://www.matematikciler.com/6-sinif/matematik-konu-anlatimlari/1020-en-kucuk-ortak-kat-ve-en-buyuk-ortak-bolen-ebob-ekok"""


def ebob(x,y):
    ebob_list=[]
    x_tam_bölen=[i for i in range(1,x+1) if x%i==0]
    y_tam_bölen=[j for j in range(1,y+1) if y%j==0]
    print("x tam bölen", x_tam_bölen)
    print("y tam bölen", y_tam_bölen)
    for k in x_tam_bölen:
        for u in y_tam_bölen:
            if k==u:
                ebob_list.append(u)
    return ebob_list[-1]          
               


print(ebob(18,24))