"""
Problem 4
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi ,
 dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. 
Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o"""

print("*"*55,"\n","*"*15,"geometrik şekil hesaplama","*"*15,"\n","*"*55,"\nÜçgen Bulmak için 3'e basın.\nDörgen Bulmak için 4'e basın.")
şekil=int(input("Cevabınız:"))

if şekil==4:
    listdörtgen=[]
    d1=abs(int(input("1.Kenar:")))
    d2=abs(int(input("2.Kenar:")))
    d3=abs(int(input("3.Kenar:")))
    d4=abs(int(input("4.Kenar:")))
    listdörtgen.append(d1)
    listdörtgen.append(d2) 
    listdörtgen.append(d3) 
    listdörtgen.append(d4) 
    listdörtgen.sort
    print(listdörtgen)
    if d1==d2==d3==d4 :
        print("Bu dörtgen bir karedir.")
    elif listdörtgen[0] == listdörtgen[1] and listdörtgen[2]==listdörtgen[3] and listdörtgen[0]!=listdörtgen[3]:
        print("Bu dörtgen bir Dikdörtgendir.")
    else:
        print("Rastgele bir dörtgendir")
elif şekil==3:
    a=abs(int(input("1.Kenar:")))
    b=abs(int(input("2.Kenar:")))
    c=abs(int(input("3.Kenar:")))
    listüçgen=[]
    listüçgen.append(a)
    listüçgen.append(b)
    listüçgen.append(c)
    listüçgen.sort()
    if a+b > c and a+c > b and b+c > a:
        if listüçgen[0] == listüçgen[1] and listüçgen[1] != listüçgen[2]:
            print("İkizkenar Üçgen")
        elif a==b==c:
            print("Eşkenar Üçgen")
        else:
            print("Rastgele Üçgen")
    else:
        print("Üçgen belirtmez.")
else:
    print("Geçecersiz Sayı girdiniz")

  