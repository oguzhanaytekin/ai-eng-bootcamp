from fastapi import FastAPI
from pydantic import BaseModel
import dbmngupdated as db  # Senin veritabanı dosyanın adı
from okul import Ogrenci
from fastapi import Query, HTTPException, status


app = FastAPI(
    title="Okul Yönetim Sistemi API",
    description="Öğrencileri yönetmek için geliştirilmiş CRUD API sistemi.",
    version="1.0.0",
)


# --- 1. SİPARİŞ FİŞİ (PYDANTIC) ---
# Kullanıcıdan veri gelirken bu kurallara uymalı
class OgrenciModel(BaseModel):
    isim: str
    soyisim: str
    numara: int


# --- 2. ANA SAYFA (GET) ---
@app.get("/", tags=["Genel"])
def ana_sayfa():
    return {"mesaj": "Okul API Sistemine Hosgeldiniz!"}


# --- 3. LİSTELEME (GET) ---
@app.get("/ogrenciler", tags=["Öğrenci İşlemleri"])
def ogrencileri_listele():
    liste = db.get_tum_ogrenciler()
    return {"veriler": liste}


@app.get("/ogrenciler/ara", tags=["Öğrenci İşlemleri"])
def ogrenci_ara(
    # Artık ikisi de "None" (Yani boş geçilebilir, zorunlu değil)
    numara: int = Query(None, description="Öğrenci Numarası"),
    isim: str = Query(None, description="Öğrenci İsmi"),
):
    # --- MANTIK KISMI ---
    if numara is not None:
        # Eski yöntem devam (Tek kişi bul)
        sonuc = db.ogrenci_bul_api(numara)

        if sonuc:
            ogrenci_data = {
                "id": sonuc[0],
                "isim": sonuc[1],
                "soyisim": sonuc[2],
                "numara": sonuc[3],
            }
            return {"mesaj": "ogrenci bulundu", "veri": ogrenci_data}
        else:
            raise HTTPException(
                status_code=404, detail=f"{numara} nolu öğrenci sistemde bulunamadı."
            )

    elif isim is not None:
        gelen_liste = db.ogrenci_bul_isimle_api(isim)

        # Eğer liste boşsa (Hiç Ahmet yoksa)
        if not gelen_liste:
            return {"mesaj": f"{isim} isminde kimse bulunamadı."}

        # Doluysa döngüye sok
        sonuclar_listesi = []
        for ogr in gelen_liste:
            veri = {"id": ogr[0], "isim": ogr[1], "soyisim": ogr[2], "numara": ogr[3]}
            sonuclar_listesi.append(veri)

        return {"mesaj": f"{isim} ismindeki öğrenciler", "veriler": sonuclar_listesi}

    else:
        return {"hata": "Kardeş ya isim ver ya numara, müneccim değilim ben."}


# --- 4. EKLEME (POST) - İŞTE EKSİK OLAN KISIM BU! ---
@app.post(
    "/ogrenciler", status_code=status.HTTP_201_CREATED, tags=["Öğrenci İşlemleri"]
)  # statuscode http201
def ogrenci_ekle(yeni_ogrenci: OgrenciModel):
    # Gelen JSON verisini, bizim eski Ogrenci nesnesine çeviriyoruz
    nesne = Ogrenci(yeni_ogrenci.isim, yeni_ogrenci.soyisim, yeni_ogrenci.numara)

    # Veritabanına kaydet
    db.ogrenci_ekle(nesne)

    return {"mesaj": f"{yeni_ogrenci.isim} başarıyla eklendi!"}


# --- 5. SİLME (DELETE) ---
# Kullanım: DELETE http://localhost:8000/ogrenciler/sil/31
@app.delete("/ogrenciler/sil/{numara}", tags=["Öğrenci İşlemleri"])
def ogrenci_sil(numara: int):

    durum = db.ogrenci_sil_api(numara)

    if durum == True:
        return {"mesaj": f"{numara} numaralı öğrenci okuldan atıldı/silindi."}
    else:
        raise HTTPException(
            status_code=404, detail="silinecek kayıt bulunamadı.zaten yok."
        )


# Kullanım: PUT http://localhost:8000/ogrenciler/guncelle/1
@app.put("/ogrenciler/guncelle/{hedef_numara}", tags=["Öğrenci İşlemleri"])
def ogrenci_guncelle(hedef_numara: int, guncel_veri: OgrenciModel):
    db.ogrenci_guncelle_api(
        hedef_numara, guncel_veri.isim, guncel_veri.soyisim, guncel_veri.numara
    )
    return {
        "mesaj": f"{hedef_numara} numaralı kayıt, {guncel_veri.isim}, {guncel_veri.soyisim}, {guncel_veri.numara} olarak güncellendi"
    }
