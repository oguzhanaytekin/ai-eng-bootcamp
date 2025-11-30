from day3pybasics import hesapla_ortalama, harf_not_belirle, sinif_durumu_hesapla


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
    tum = [a["Ortalama"] for a in liste]
    sinif_ort = sum(tum) / len(liste)
    return sinif_ort
