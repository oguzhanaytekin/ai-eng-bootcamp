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
    cursor.execute(komut)  # ogrenciler tablo komutu
    komut2 = """
    CREATE TABLE IF NOT EXISTS notlar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ogrenci_id INTEGER,
    ders_adi TEXT,
    puan INTEGER,
    FOREIGN KEY(ogrenci_id) REFERENCES ogrenciler(id)
    
    )
    """
    cursor.execute(komut2)  # not tablo komutu

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
    print("ogrenci ve not tablosu hazir.")


def not_ekle(ogrenci_id, ders, puan):
    conn = baglanti_kur()
    cursor = conn.cursor()
    komutt = "INSERT INTO notlar(ogrenci_id,ders_adi,puan) VALUES (?,?,?)"
    cursor.execute(komutt, (ogrenci_id, ders, puan))
    conn.commit()
    conn.close()
    print(f"{ogrenci_id} icin {ders} dersi puani: {puan}")


def ogrenci_goster():
    conn = baglanti_kur()
    cursor = conn.cursor()

    komut = "SELECT * from ogrenciler"
    cursor.execute(komut)

    liste = cursor.fetchall()  # bulduğun her şeyi liste formunda getir.

    for ogr in liste:
        print(f"ID: {ogr[0]} || {ogr[1]} {ogr[2]} || No:{ogr[3]}")

    conn.close()


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


def karne(ogrenci_id):
    conn = baglanti_kur()
    cursor = conn.cursor()
    komut = """
    SELECT ogrenciler.isim, ogrenciler.soyisim, notlar.ders_adi, notlar.puan
    FROM notlar
    JOIN ogrenciler ON notlar.ogrenci_id= ogrenciler.id
    WHERE ogrenciler.id = ?
    """
    cursor.execute(komut, (ogrenci_id,))
    sonuclar = cursor.fetchall()
    conn.close()

    # JOIN BÜYÜSÜ BURADA!
    # Diyoruz ki: notlar tablosunu al, yanına ogrenciler tablosunu yapıştır.
    # Ama neye göre? notlar.ogrenci_id = ogrenciler.id olanları eşleştir!

    if not sonuclar:
        print(f"{ogrenci_id} icin sonuc bulunamadı.")

        print(f"\n🎓 {sonuclar[0][0]} {sonuclar[0][1]} İÇİN KARNE:")
        print("-" * 30)
    ortalama_toplam = 0
    for satir in sonuclar:
        # satir = ('Victor', 'Osimhen', 'Fizik', 45)
        ders = satir[2]
        puan = satir[3]
        print(f"📘 {ders}: {puan}")
        ortalama_toplam += puan
        ort = ortalama_toplam / len(sonuclar)
        print("-" * 30)
        print(f"📊 ORTALAMA: {ort:.2f}")


if __name__ == "__main__":
    tablo_olustur()  # kodu test et
    ogrenci_goster()
    not_ekle(1, "fizik", 45)
    karne(1)
