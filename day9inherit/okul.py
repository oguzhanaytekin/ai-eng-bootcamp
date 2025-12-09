class Kisi:
    def __init__(self, isim, soyisim):
        self.isim = isim
        self.soyisim = soyisim

    def kimlik(self):
        return f"Ad: {self.isim} Soyad: {self.soyisim} (Default)"


class Ogrenci(Kisi):
    def __init__(self, isim, soyisim, stu_id):

        super().__init__(isim, soyisim)
        self.stu_id = stu_id

    def kimlik(self):
        temelbilgi = super().kimlik()
        return f"Info: {temelbilgi}, No:{self.stu_id} (Ogrenci)"


class Ogretmen(Kisi):
    def __init__(self, isim, soyisim, brans):
        super().__init__(isim, soyisim)
        self.brans = brans

    def kimlik(self):
        temel_bilgi = super().kimlik()
        return f"Info: {temel_bilgi}, {self.brans} (Ogretmen)"


k1 = Kisi("oguzhan", "aytekin")
o1 = Ogrenci("osman", "osman", "123")
t1 = Ogretmen("mahmut", "mama", "matematik")

print(k1.kimlik())
print(o1.kimlik())
print(t1.kimlik())

# polymorphism testi##########################################
print("\n--- OKUL NÜFUSU YOKLAMASI ---")

# Farklı türdeki nesneleri aynı listeye koyuyoruz
okul_nufusu = [k1, o1, t1]  # Farklı türdeki nesneleri aynı listeye koyuyoruz

for kisi in okul_nufusu:
    print(
        kisi.kimlik()
    )  #  Büyü burada: 'kisi' değişkeni her turda farklı bir Class'a dönüşüyor. Ama Python umursamıyor, çünkü hepsinde 'kimlik()' metodu var.


# polymorphism testi###########################################
