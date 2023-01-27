print("""-------------------------------------------------
Hesap Makinesi Programına Hoşgeldiniz 
İşlemler;
1. Toplama İşlemi
2. Çıkarma İşlemi
3. Çarpma İşlemi
4. Bölme İşlemi
-----------------------------------------------------------
""")

a= int(input("Yapmak istedğiniz işlemin numarasını giriniz."))
if a<1 or a>4:
    print("Geçersiz işlem numarası girdiniz. Lütfen girdiğiniz numarayı kontrol ediniz...")
    exit

else:
    say_1= float(input("İşleme sokmak istediğiniz birinci sayıyı giriniz :"))
    say_2= float(input("İşleme sokmak istediğiniz ikinci sayıyı giriniz :"))

    if a==1:
        print("{} + {} = {} ".format(say_1,say_2,say_1+say_2))
    elif a==2:
        print("{} - {} = {} ".format(say_1,say_2,say_1-say_2))
    elif a==3:
        print("{} x {} = {} ".format(say_1,say_2,say_1*say_2))
    elif a==4:
        print("{} / {} = {} ".format(say_1,say_2,say_1/say_2))

