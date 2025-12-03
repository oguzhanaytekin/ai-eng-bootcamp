from ogrenci import Ogrenci


def main():
    sinif_listesi = []
    while True:
        isim = input("ogrenci adi:(q cikis)")
        if isim.lower() == "q":
            break

        try:

            v = int(input("vize:"))
            f = int(input("final:"))

            if not (0 <= v <= 100 and 0 <= f <= 100):
                print("0-100 arası degerler!")
                continue
        except ValueError:
            print("sayi gir")
            continue

        yeni_ogr = Ogrenci(isim, v, f)
        yeni_ogr.durum_hesapla()
        sinif_listesi.append(yeni_ogr)

        print(f"{yeni_ogr.bilgi_goster()}")


main()
