from okul import Ogrenci

import sqlite3


def baglanti_kur():
    connection = sqlite3.connect("okul.db")
    return connection


def tablo_olustur():
    conn = baglanti_kur()
    cursor = conn.cursor()  # db üzerinde işlem yapan imlec

    komut = """
    CREATE TABLE IF NOT EXISTS ogrenciler (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        isim TEXT,
        soyisim TEXT,
        numara INTEGER
    )
    """

    cursor.execute(komut)  # Komutu çalıştır
    conn.commit()  # Değişikliği kaydet
    conn.close()  # Bağlantıyı kapat
    print("Veritabanı ve Tablo başarıyla oluşturuldu/kontrol edildi.")


def ogrenci_ekle(ogrenci_nesnesi):
    conn = baglanti_kur()
    cursor = conn.cursor()

    komut = "INSERT INTO ogrenciler (isim,soyisim,numara) VALUES(? ,? ,?)"  # ? SQL injection engellemek icin
    cursor.execute(
        komut, (ogrenci_nesnesi.isim, ogrenci_nesnesi.soyisim, ogrenci_nesnesi.stu_id)
    )

    conn.commit()  # yazılmadığı takdirde veri ramde kalır dosyaya yazılmaz.
    conn.close()
    print(f"{ogrenci_nesnesi.isim}{ogrenci_nesnesi.soyisim} nesne olarak eklendi!")


def ogrenci_goster():
    conn = baglanti_kur()
    cursor = conn.cursor()

    komut = "SELECT * from ogrenciler"
    cursor.execute(komut)

    liste = cursor.fetchall()  # bulduğun her şeyi liste formunda getir.

    for ogr in liste:
        print(f"ID: {ogr[0]} || {ogr[1]} {ogr[2]} || No:{ogr[3]}")

    conn.close()


if __name__ == "__main__":
    tablo_olustur()  # kodu test et


yeniogr = Ogrenci("Victor", "Osimhen", 45)
ogrenci_ekle(yeniogr)

ogrenci_goster()


def ogrenci_bul(aranan_numara):
    conn = baglanti_kur()
    cursor = conn.cursor()

    komut = "SELECT * FROM ogrenciler WHERE numara= ? "
    cursor.execute(komut, (aranan_numara,))  # tek elemanlı tuple için virgül şart

    sonuc = cursor.fetchone()  # unique değer döndürcez.

    conn.close()

    if sonuc:
        print(f"{sonuc[1]}  {sonuc[2]}  {sonuc[3]}")

    else:
        print(f"{aranan_numara} bulunamadı")


ogrenci_bul(45)

ogrenci_bul(31)
