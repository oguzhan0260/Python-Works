"""
Problem 3
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.


    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF

"""
print("*"*15,"Harf Notu Hesaplayıcı","*"*15)

v1=int(input("Vize1:"))
v2=int(input("Vize2:"))
f=int(input("Final:"))

ort= (v1*30/100)+ (v2*30/100)+(f*40/100)
print(ort)

if ort>=90:
    print( "Harf NOTUN: AA")
elif ort<90 and ort>=85:
    print( "Harf NOTUN: BA")
elif ort<85 and ort>=80:
    print( "Harf NOTUN: BB")
elif ort<80 and ort>=75:
    print( "Harf NOTUN: CB")
elif ort<75 and ort>=70:
    print( "Harf NOTUN: CC")
elif ort<70 and ort>=65:
    print( "Harf NOTUN: DC")
elif ort<65 and ort>=60:
    print( "Harf NOTUN: DD")
elif ort<60 and ort>=55:
    print( "Harf NOTUN: FD")
elif ort<55 :
    print( "Harf NOTUN: FF")

    
