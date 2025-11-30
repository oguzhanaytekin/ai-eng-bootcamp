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


def sinif_durumu_hesapla(liste):
    # 1. GÜVENLİK KONTROLÜ: Liste boş mu?
    if len(liste) == 0:
        return 0  # Liste boşsa ortalama 0'dır, hesap yapmaya çalışma.

    # 2. Liste doluysa hesapla
    tum = [a["Ortalama"] for a in liste]
    sinif_ort = sum(tum) / len(liste)

    return sinif_ort


def main():
    liste = []

    while True:
        isim_input = input("Ogrenci adi giriniz:")
        if isim_input.lower() == "q":
            break
        try:

            vize = int(input("Vize notu giriniz:"))
            if 0 <= vize <= 100:
                continue
            else:
                print("vize notu 0 ile 100 arasında olmalı.")

            final = int(input("Final Notu giriniz."))
            if final >= 0 and final <= 100:
                continue
            else:
                print("final notu 0 ile 100 arasında olmalı.")
        except ValueError:
            print("SADECE SAYISAL DEGER")
            continue  ##########

        avg = hesapla_ortalama(vize, final)
        durum = harf_not_belirle(avg)
        ogrenci = {"İsim": isim_input, "Ortalama": avg, "Durum": durum}

        liste.append(ogrenci)

    sonuc = sinif_durumu_hesapla(liste)
    print(f"sinif ortalaması:  {sonuc}")


main()
