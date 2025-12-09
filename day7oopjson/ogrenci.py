class Ogrenci:

    def __init__(self, isim, vize, final):
        self.isim = isim
        self.__vize = vize
        self.__final = final
        self.ortalama = 0
        self.durum = ""

    def ortalama_hesapla(self):
        sonuc = self.__vize * 0.4 + self.__final * 0.6
        self.ortalama = float(sonuc)

    def durum_hesapla(self):
        self.ortalama_hesapla()
        if self.ortalama < 50:
            self.durum = "kaldiniz"
        elif 50 <= self.ortalama <= 85:
            self.durum = "gecti"
        else:
            self.durum = "Tebrikler AA."

    def __str__(self):
        return f"{self.isim} {self.__vize} {self.__final} {self.ortalama} {self.durum}"

    ##################### SERIALIZATION
    # nesneyi sozluge cevirme (kayit icin)
    def to_dict(self):
        return {"isim": self.isim, "vize": self.__vize, "final": self.__final}

    # sozlukten nesne yaratma (dosya okumasi icin)
    @classmethod
    def from_dict(cls, veri_sozlugu):

        return cls(veri_sozlugu["isim"], veri_sozlugu["vize"], veri_sozlugu["final"])

    @property
    def vize(self):
        return self.__vize

    @property
    def final(self):
        return self.__final

    @vize.setter
    def vize(self, yeni_vize):
        if 0 <= self.__vize <= 100:
            self.__vize = yeni_vize
        else:
            print("vize 0 ile 100 arasinda olmali")

    @final.setter
    def final(self, yeni_final):
        if 0 <= self.__final <= 100:
            self.__final = yeni_final
        else:
            print("final 0 ile 100 arasinda olmali")
