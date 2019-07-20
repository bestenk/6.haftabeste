class personel :
    baslangic_maas = 1.400
    def __init__(self,ad,soyad,telefon):
      self.ad = ad
      self.soyad = soyad
      self.telefon = telefon

    def tamadi(self):
        return "{} {}".format(self.ad, self.soyad)
    def telefon(self):
        return "+(90){}".format(self.telefon)


    def __str__(self):
        return "{} {} {}".format(self.ad, self.soyad, self.telefon)


class yazilimci(personel):
    baslangic_maas = 10.000

    def __init__(self,ad, soyad, telefon, yazilimdili):
        super().__init__(ad,soyad,telefon) #miras aldığımız sınıfın constructor(yapıcı metot) (__init__) değerine parametre gönderiyoruz
        self.yazilimdili = yazilimdili

    def __str__(self):
        return "{} {}".format(super().__str__(),self.yazilimdili)

Personel = personel("beste","karademir","2258412")
Yazilimci = yazilimci("beste","karademir","4568328","python")

print(Personel)
print(Yazilimci)

print(issubclass(personel, yazilimci))
print(issubclass(yazilimci, personel)) # personel yazılımcı class ın alt sınıfıdır