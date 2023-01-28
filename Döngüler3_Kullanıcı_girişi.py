print("**********\nKullanıcı Girişi\n**********\n")

# K

sys_kul_adı = "ooguzhan" # Sistemde Kayıtlı Olduğunu Düşündüğümüz Kullanıcı Adı

sys_parola  = "12345" # Sistemde Kayıtlı Olduğunu Düşündüğümüz Parola

while True:
    ad_input=input("Kullanıcı Adınız:")
    şifre_giriş=input("Şifrenizi Giriniz:")
    if ad_input == sys_kul_adı and şifre_giriş==sys_parola:
        print("Sisteme Giriş Yapılıyor...")
        break
    else :
        print("Yanlış şifre veya kullanıcı adı.Tekrar deneyiniz.\n\n")


