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


def ogrenci_ekle(isim, soyisim, numara):
    conn = baglanti_kur()
    cursor = conn.cursor()

    komut = "INSERT INTO ogrenciler (isim,soyisim,numara) VALUES(? ,? ,?)"  # ? SQL injection engellemek icin
    cursor.execute(komut, (isim, soyisim, numara))

    conn.commit()  # yazılmadığı takdirde veri ramde kalır dosyaya yazılmaz.
    conn.close()
    print(f"{isim} {soyisim} eklendi!")


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


ogrenci_ekle("oguzhan", "aytekin", "10")
ogrenci_ekle("osman", "osman", "31")


ogrenci_goster()
