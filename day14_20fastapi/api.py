from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from routers import ogrenciler  # <--- Oluşturduğumuz dosyayı çağırıyoruz

# --- Uygulamayı Başlat ---
app = FastAPI(
    title="Okul Yönetim Sistemi API",
    version="2.0 (Professional)",
    description="Router yapısına geçmiş, modüler ve asenkron mimari.",
)
app.mount("/dosyalar", StaticFiles(directory="yuklenenler"), name="static")
# --- Router'ları (Departmanları) Bağla ---
# Gelen istek 'öğrenci işlemi' ise, o dosyaya yönlendir:
app.include_router(ogrenciler.router)


# --- Ana Kapı (Karşılama) ---
@app.get("/", tags=["Genel"])
async def ana_sayfa():
    return {"mesaj": "Sistem Ayakta! Router Modu Devrede. 🚀"}
