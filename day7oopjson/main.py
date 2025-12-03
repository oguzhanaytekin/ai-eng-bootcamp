import json
import os
from ogrenci import Ogrenci

# Dosya adını sabitleyelim, karışıklık olmasın
DOSYA_ADI = "veri.json"


# --- OKUMA (LOAD) FONKSİYONU ---
def verileri_yukle():
    # Dosya yoksa boş liste döndür (İlk çalıştırışta hata vermesin)
    if not os.path.exists(DOSYA_ADI):
        return []

    # 1. Dosyayı "r" (READ/OKUMA) modunda açıyoruz
    with open(DOSYA_ADI, "r", encoding="utf-8") as f:
        # JSON listesini (sözlükler listesi) çekiyoruz
        ham_liste = json.load(f)

    canli_liste = []

    # 2. Sözlükleri Nesneye Çevirme Döngüsü
    for sozluk in ham_liste:
        # Sözlükten --> Ogrenci Nesnesi yarat
        nesne = Ogrenci.from_dict(sozluk)

        # Nesne oluştu ama ortalaması 0, hemen hesaplatıyoruz
        nesne.durum_hesapla()

        # Listeye ekle
        canli_liste.append(nesne)

    return canli_liste


# --- KAYDETME (SAVE) FONKSİYONU ---
def verileri_kaydet(liste):
    kaydedilecek_liste = []

    # Nesneleri --> Sözlüğe Çevirme Döngüsü
    for ogr in liste:
        kaydedilecek_liste.append(ogr.to_dict())

    # Dosyayı "w" (WRITE/YAZMA) modunda açıyoruz
    with open(DOSYA_ADI, "w", encoding="utf-8") as f:
        json.dump(kaydedilecek_liste, f, indent=4)

    print("💾 Veriler başarıyla kaydedildi.")


# --- ANA PROGRAM ---
def main():
    # Başlangıçta verileri yükle
    sinif_listesi = verileri_yukle()
    print(f"\n♻️ {len(sinif_listesi)} eski kayıt yüklendi.")

    # Mevcut listeyi bir gösterelim (Opsiyonel)
    for ogr in sinif_listesi:
        print(ogr.bilgi_goster())

    while True:
        print("\n--- YENİ GİRİŞ ---")
        isim = input("Öğrenci Adı ('q' çıkış): ")
        if isim.lower() == "q":
            break

        try:
            v = int(input("Vize: "))
            f = int(input("Final: "))

            if not (0 <= v <= 100 and 0 <= f <= 100):
                print("Hata: 0-100 arası gir!")
                continue

            # Yeni nesne yarat
            yeni_ogr = Ogrenci(isim, v, f)
            yeni_ogr.durum_hesapla()  # Anlık görmek için hesapla

            # Listeye ekle
            sinif_listesi.append(yeni_ogr)
            print(f"✅ Eklendi: {yeni_ogr.bilgi_goster()}")

        except ValueError:
            print("Lütfen sayı giriniz.")
            continue

    # Çıkarken kaydet
    verileri_kaydet(sinif_listesi)
    print("👋 Program kapatılıyor...")


if __name__ == "__main__":
    main()
