

class  person:
    firstname = "",
    lastname  = "",
    phone     = "",
    mail      = "",

    def  __str__(self):
        return  "{} {}".format(self.firstname, self.lastname)

    def Bul(self, kelime):
        if kelime in self.firstname or kelime in self.lastname or kelime in self.mail or kelime in self.phone:
            return True
        else:
            return False



kisiler = []
isimler = ["simge","furkan","rabia","başak","çağla","dilara","elif","erdener","okan","mahmut"]
soyisimler = ["karademir","başkent","tüylek","şentürk","çandır","garip","pambuk","kaya","muzikacı","tok"]

# default olarak kulanıcı ekliyoruz
import random
for i in range (10):
    kisi = person()
    kisi.firstname = random.choice(isimler)
    kisi.lastname  = random.choice(soyisimler).upper()
    kisi.mail      = "{} {}@bilgeadam.ccm".format(kisi.firstname,kisi.lastname)
    kisi.phone     = "+(90)5{} {} {}".format("32", "352", "09","97")

    kisiler.append(kisi)


def Liste(kelime = ""):
    if kelime == "":
        index = 0
        for kisi in kisiler:
           print("-" * 50)
           print("id : {}\nkisi adı : {}\nkisi soyadı : {}\nkisi telefon : {}\nkisi mail : {}".format(index,kisi.firstname,kisi.lastname,kisi.phone,kisi.mail))
           index += 1

    else:
        for kisi in kisiler:
            index = 0
            if kisi.Bul(kelime):

              print("-" * 50)
              print("id : {}\nkisi adı : {}\nkisi soyadı : {}\nkisi telefon : {}\nkisi mail : {}".format(index,kisi.firstname,kisi.lastname,kisi.phone,kisi.mail))
              index += 1
        print("kişiyi bul")



def main():
    ekle     = "a"
    sil      = "d"
    guncelle = "u"
    liste    = "l"
    bul      = "f"
    islem    = ""
    go_on    = "y"
    result  = True

    while True :

        print ("lütfen yapmak istediğiniz işlemi seçin")
        print("-" * 32)
        print("kişi eklemek için : a\nkişi silmek için : d\nkişi güncellemek için : u\nkişi listelemek için : l\nkişi bulmak için : f ")
        print("-" * 32)
        islem = input("lütfen bir anahtar kelime seçiniz")

        if islem == "a" :
            kisi = person()
            kisi.firstname = input("adınız : ")
            kisi.lastname  = input("soyadınız : ")
            kisi.phone     = input("telefon numaranız : ")
            kisi.mail      = input("mail adresiniz : ")

            kisiler.append(kisi)
            print("kişi rehbere eklendi")


        elif islem == "d" :
            Liste()


            id = int(input("silmek istediğiniz kişinin id değerini girin : "))
            kisiler.remove(kisiler[id])
            print("silindi")
        elif islem == "u":
            Liste()

            id = int(input("lütfen güncellemek istediğiniz kişinin if değerini girin : "))

            update_person = kisiler[id]
            update_person.firstname = input("adınız : ")
            update_person.lastname  = input("soyadınız : ")
            update_person.phone     = input("telefon numaranız : ")
            update_person.mail      = input("mail adresiniz : ")
            print("guncellendi")

        elif islem == "l":
            Liste()
            print("kişi listesi")
        elif islem == "f":
           Liste(input("lütfen anahtar kelimeyi girin : "))
           print("kişi bilgieri")
        else :
            result = False
            print("rehber uygulamasından çıkış sağlandı")
        print("devam etmek için herhangi bir tuşa basın")


main()