def hesapla_ortalama(vize, final):
    ort = 0.4 * vize + 0.6 * final
    ortalama = float(ort)
    return ortalama


def harf_not_belirle(ortalama):
    if ortalama < 50:
        return "Kaldiniz"
    elif ortalama > 50 and ortalama < 80:
        return "Gectiniz"
    else:
        return "Tebrikler (AA)"


def sinif_durumu_hesapla(liste):
    tum = [a["Ortalama"] for a in liste]
    sinif_ort = sum(tum) / len(liste)
    return sinif_ort


def main():
    liste = []

    while True:
        isim_input = input("Ogrenci adi giriniz:")
        if isim_input == "q".lower():
            break
        vize = int(input("Vize notu giriniz:"))
        final = int(input("Final Notu giriniz."))

        avg = hesapla_ortalama(vize, final)
        durum = harf_not_belirle(avg)
        ogrenci = {"İsim": isim_input, "Ortalama": avg, "Durum": durum}

        liste.append(ogrenci)

    sonuc = sinif_durumu_hesapla(liste)
    print(f"sinif ortalaması:  {sonuc}")


main()
