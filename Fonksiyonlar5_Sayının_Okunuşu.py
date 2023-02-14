""" Problem 4
Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.

Örnek: 97 ---------> Doksan Yedi"""


def number_reader(say):
    Tens_reader="Tens Reader"
    Ones_reader="Ones Reader"
    tens_digit= say//10
    ones_digit= say%10

    if tens_digit==1:
        Tens_reader="On"
    elif tens_digit==2:
        Tens_reader="Yirmi"
    elif tens_digit==3:
        Tens_reader="Otuz"
    elif tens_digit==4:
        Tens_reader="Kırk"
    elif tens_digit==5:
        Tens_reader="Elli"
    elif tens_digit==6:
        Tens_reader="Altmış"
    elif tens_digit==7:
        Tens_reader="Yetmiş"
    elif tens_digit==8:
        Tens_reader="Seksen"
    elif tens_digit==9:
        Tens_reader="Doksan"

    if ones_digit==1:
        Ones_reader="Bir"
    elif ones_digit==2:
        Ones_reader="İki"
    elif ones_digit==3:
        Ones_reader="Üç"
    elif ones_digit==4:
        Ones_reader="Dört"
    elif ones_digit==5:
        Ones_reader="Beş"
    elif ones_digit==6:
        Ones_reader="Altı"
    elif ones_digit==7:
        Ones_reader="Yedi"
    elif ones_digit==8:
        Ones_reader="Sekiz"
    elif ones_digit==9:
        Ones_reader="Dokuz"
    elif ones_digit==0:
        Ones_reader=""

    return Tens_reader +" "+ Ones_reader
    


say =  int(input("Sayı:"))
print(number_reader(say))
