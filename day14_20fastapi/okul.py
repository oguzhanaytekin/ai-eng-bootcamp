from abc import ABC, abstractmethod


class Kisi(ABC):
    def __init__(self, isim, soyisim):
        self.isim = isim
        self.soyisim = soyisim

    @abstractmethod
    def kimlik(self):
        # return f"Ad: {self.isim} Soyad: {self.soyisim} (Default)"  # abstract class olunca bu tanımlamayı yapamıyoruz.(kisinin kimligi olmaz alt sınıfların olur.)
        pass


class Ogrenci(Kisi):
    def __init__(self, isim, soyisim, stu_id):

        super().__init__(isim, soyisim)
        self.stu_id = stu_id

    def kimlik(self):
        # temelbilgi = super().kimlik() #abstract olunca pasifize oldu
        return f"Ad: {self.isim} Soyad: {self.soyisim} No:{self.stu_id} (Ogrenci)"  # abstract class olunca bu tanımlamayı yapamıyoruz.(kisinin kimligi olmaz alt sınıfların olur.)


class Ogretmen(Kisi):
    def __init__(self, isim, soyisim, brans):
        super().__init__(isim, soyisim)
        self.brans = brans

    def kimlik(self):
        # temel_bilgi = super().kimlik() #pasifize oldu.
        return f"Ad: {self.isim} Soyad: {self.soyisim} No:{self.brans} (Ogretmen)"


# k1 = Kisi("oguzhan", "aytekin") #abstract oldu.
o1 = Ogrenci("osman", "osman", "123")
t1 = Ogretmen("mahmut", "mama", "matematik")

# print(k1.kimlik()) abstract oldu.
print(o1.kimlik())
print(t1.kimlik())

# polymorphism testi##########################################
print("\n--- OKUL NÜFUSU YOKLAMASI ---")

# Farklı türdeki nesneleri aynı listeye koyuyoruz
# okul_nufusu = [k1,o1, t1]  # Farklı türdeki nesneleri aynı listeye koyuyoruz #k1 abstract oldu

okul_nufusu = [o1, t1]
for kisi in okul_nufusu:
    print(
        kisi.kimlik()
    )  #  Büyü burada: 'kisi' değişkeni her turda farklı bir Class'a dönüşüyor. Ama Python umursamıyor, çünkü hepsinde 'kimlik()' metodu var.


# polymorphism testi###########################################


class Mudur(Kisi):
    pass


# m1 = Mudur("kel", "mahmut") #TypeError: Can't instantiate abstract class Mudur without an implementation for abstract method 'kimlik'
