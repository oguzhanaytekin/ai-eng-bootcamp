class Ogrenci:

    def __init__(self, isim, vize, final):
        self.isim = isim
        self.vize = vize
        self.final = final
        self.ortalama = 0
        self.durum = ""

    def ortalama_hesapla(self):
        sonuc = self.vize * 0.4 + self.final * 0.6
        self.ortalama = float(sonuc)

    def durum_hesapla(self):
        self.ortalama_hesapla()
        if self.ortalama < 50:
            self.durum = "kaldiniz"
        elif 50 <= self.ortalama <= 85:
            self.durum = "gecti"
        else:
            self.durum = "Tebrikler AA."

    def bilgi_goster(self):
        return f"Ogrenci: {self.isim} Ort:{self.ortalama} Durum: {self.durum}"
