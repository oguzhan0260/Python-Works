"""TAM BÖLENLERİ BULMA FONKSİYONU"""

def tambölenler(say):
    liste=[ i for i in range(2,say) if say%i==0]
    return liste

while True:
    say= input("Çıkmak için q basınız\nSayı:")
    if say=="q":
        break
    else:
        say=int(say)
        print("Tam Bölenler:", tambölenler(say))