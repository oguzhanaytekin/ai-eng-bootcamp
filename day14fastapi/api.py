from fastapi import FastAPI
from pydantic import BaseModel
import dbmngupdated as db  # Senin veritabanı dosyanın adı
from okul import Ogrenci

app = FastAPI()


# --- 1. SİPARİŞ FİŞİ (PYDANTIC) ---
# Kullanıcıdan veri gelirken bu kurallara uymalı
class OgrenciModel(BaseModel):
    isim: str
    soyisim: str
    numara: int


# --- 2. ANA SAYFA (GET) ---
@app.get("/")
def ana_sayfa():
    return {"mesaj": "Okul API Sistemine Hosgeldiniz!"}


# --- 3. LİSTELEME (GET) ---
@app.get("/ogrenciler")
def ogrencileri_listele():
    liste = db.get_tum_ogrenciler()
    return {"veriler": liste}


# --- 4. EKLEME (POST) - İŞTE EKSİK OLAN KISIM BU! ---
@app.post("/ogrenciler")
def ogrenci_ekle(yeni_ogrenci: OgrenciModel):
    # Gelen JSON verisini, bizim eski Ogrenci nesnesine çeviriyoruz
    nesne = Ogrenci(yeni_ogrenci.isim, yeni_ogrenci.soyisim, yeni_ogrenci.numara)

    # Veritabanına kaydet
    db.ogrenci_ekle(nesne)

    return {"mesaj": f"{yeni_ogrenci.isim} başarıyla eklendi!"}
