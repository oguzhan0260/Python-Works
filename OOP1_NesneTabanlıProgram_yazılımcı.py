""""
Örnegin öğrenci otomasyon sistemi yazmak istiyoruz. Bunun için öğrencileri, öğretmeneler i ve kursaları birer enesne olarak 
oluşturmamız gerekiyor.

"""

class yazılımcı():

    def __init__(self,ad,soyad,yaş,diller,maaş):
        self.ad= ad
        self.soyad= soyad
        self.yaş= yaş
        self.diller= diller
        self.maaş= maaş

    def bilgileri_sorgula(self):
        print("""
        Yazılımcının Bilgileri
        AD:{}
        SOYAD:{}
        YAŞ:{}
        DİLLER:{}
        MAAŞ:{}
        
        """.format(self.ad,self.soyad,self.yaş,self.diller,self.maaş))

    def maaş_zam(self,zam_miktar):
        self.maaş +=zam_miktar
        print("Zam Yapıldı. Yeni Maaş:",self.maaş)


ozzie= yazılımcı("Oğuzhan","Sürmeli",23,"Python",8000)

ozzie.bilgileri_sorgula()
ozzie.maaş_zam(1000)

