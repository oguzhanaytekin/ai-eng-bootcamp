import json
import os
from day5json import *


def hesapla_ortalama(vize, final):
    ort = 0.4 * vize + 0.6 * final
    ortalama = float(ort)
    return ortalama


def harf_not_belirle(ortalama):
    if ortalama < 50:
        return "Kaldiniz"
    elif ortalama >= 50 and ortalama < 80:
        return "Gectiniz"
    else:
        return "Tebrikler (AA)"


def sinif_durumu_hesapla(ogrenci_liste):
    # 1. GÜVENLİK KONTROLÜ: Liste boş mu?
    if len(ogrenci_liste) == 0:
        return 0  # Liste boşsa ortalama 0'dır, hesap yapmaya çalışma.

    # 2. Liste doluysa hesapla
    tum = [a["Ortalama"] for a in ogrenci_liste]
    sinif_ort = sum(tum) / len(ogrenci_liste)

    return sinif_ort


def load_veriler():
    if os.path.exists("ogrenciler.json"):
        with open("ogrenciler.json", "r", encoding="utf-8") as dosya:
            return json.load(dosya)
    else:

        return []


def save_veriler(liste):
    with open("ogrenciler.json", "w", encoding="utf-8") as dosya:
        json.dump(liste, dosya, indent=4)
    print("veriler basariyla kaydedildi..")


def main():
    ogrenci_liste = load_veriler()

    while True:
        isim_input = input("Ogrenci adi giriniz:")
        if isim_input.lower() == "q":
            break
        try:

            vize = int(input("Vize notu giriniz:"))
            final = int(input("Final Notu giriniz."))
            if not (0 <= vize <= 100 and 0 <= final <= 100):
                continue

        except ValueError:
            print("SADECE SAYISAL DEGER")
            continue  ##########

        avg = hesapla_ortalama(vize, final)
        durum = harf_not_belirle(avg)
        ogrenci = {"İsim": isim_input, "Ortalama": avg, "Durum": durum}

        ogrenci_liste.append(ogrenci)
    save_veriler(ogrenci_liste)
    sonuc = sinif_durumu_hesapla(ogrenci_liste)
    print(f"sinif ortalaması:  {sonuc}")
    print(f"listenin son durumu: {ogrenci_liste}")


main()
