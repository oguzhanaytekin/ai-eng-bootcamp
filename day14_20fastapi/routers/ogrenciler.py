from fastapi import APIRouter, HTTPException, status, Query
from pydantic import BaseModel, Field
from typing import Optional

# Ana dizindeki veritabanı dosyalarını çağırıyoruz
import dbmngupdated as db
from okul import Ogrenci

# --- ROUTER KURULUMU (Artık 'app' değil 'router' var) ---
router = APIRouter(
    tags=["Öğrenci İşlemleri"]  # Swagger'daki başlık burada otomatik tanımlanır
)


# --- Veri Modeli (Buraya taşındı) ---
class OgrenciModel(BaseModel):
    isim: str = Field(..., min_length=2, max_length=30, description="Öğrencinin adı")
    soyisim: str = Field(
        ..., min_length=2, max_length=30, description="Öğrencinin soyadı"
    )
    numara: int = Field(..., gt=0, le=10000, description="Okul numarası")


# --- ENDPOINTLER (Hepsi async ve @router oldu) ---


# 1. Listeleme
@router.get("/ogrenciler")
async def ogrencileri_listele():
    liste = db.get_tum_ogrenciler()
    return {"veriler": liste}


# 2. Arama
# --- 2. Arama (Gelişmiş Versiyon) ---
@router.get("/ogrenciler/ara")
async def ogrenci_ara(
    numara: Optional[int] = Query(None, description="Tam numara araması"),
    isim: Optional[str] = Query(
        None, min_length=2, description="İsim içinde geçen harfler"
    ),
):
    # ÖNCELİK 1: Numara varsa, tekil sonuç döner (Kesinlik)
    if numara is not None:
        sonuc = db.ogrenci_bul_api(numara)
        if sonuc:
            return {
                "mesaj": "Numara ile bulundu",
                "veri": {
                    "id": sonuc[0],
                    "isim": sonuc[1],
                    "soyisim": sonuc[2],
                    "numara": sonuc[3],
                },
            }
        else:
            raise HTTPException(status_code=404, detail="Bu numarada öğrenci yok.")

    # ÖNCELİK 2: İsim varsa, liste döner (Esneklik)
    elif isim is not None:
        gelen_liste = db.ogrenci_bul_isimle_api(isim)  # Artık LIKE ile çalışıyor

        if not gelen_liste:
            raise HTTPException(
                status_code=404, detail=f"'{isim}' içeren kimse bulunamadı."
            )

        sonuclar = []
        for ogr in gelen_liste:
            sonuclar.append(
                {"id": ogr[0], "isim": ogr[1], "soyisim": ogr[2], "numara": ogr[3]}
            )

        return {
            "mesaj": f"İçinde '{isim}' geçen {len(sonuclar)} kayıt bulundu.",
            "veriler": sonuclar,
        }

    else:
        raise HTTPException(
            status_code=400, detail="Arama yapmak için parametre giriniz."
        )


# 3. Ekleme
@router.post("/ogrenciler", status_code=status.HTTP_201_CREATED)
async def ogrenci_ekle(yeni_ogrenci: OgrenciModel):
    # Duplicate Check
    mevcut = db.ogrenci_bul_api(yeni_ogrenci.numara)
    if mevcut:
        raise HTTPException(status_code=400, detail="Bu numara zaten kayıtlı!")

    nesne = Ogrenci(yeni_ogrenci.isim, yeni_ogrenci.soyisim, yeni_ogrenci.numara)
    db.ogrenci_ekle(nesne)
    return {"mesaj": f"{yeni_ogrenci.isim} eklendi."}


# 4. Silme
@router.delete("/ogrenciler/sil/{numara}")
async def ogrenci_sil(numara: int):
    if not db.ogrenci_sil_api(numara):
        raise HTTPException(status_code=404, detail="Silinecek kayıt yok.")
    return {"mesaj": f"{numara} silindi."}


# 5. Güncelleme
@router.put("/ogrenciler/guncelle/{hedef_numara}")
async def ogrenci_guncelle(hedef_numara: int, guncel_veri: OgrenciModel):
    db.ogrenci_guncelle_api(
        hedef_numara, guncel_veri.isim, guncel_veri.soyisim, guncel_veri.numara
    )
    return {"mesaj": "Güncelleme başarılı."}
