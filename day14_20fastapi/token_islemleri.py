import jwt
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer


# 1. GİZLİ ANAHTAR (Bunu sadece sunucu bilecek, token'ların taklit edilmesini engeller)
SECRET_KEY = "benim_cok_gizli_anahtarim_kimse_bilmesin"
ALGORITHM = "HS256"
TOKEN_SURESI_DAKIKA = 30  # VIP kart 30 dakika sonra çöp olsun


def token_olustur(veri: dict):
    kopyalanacak_veri = veri.copy()

    # Şu anki saate 30 dakika ekleyip bitiş (exp) zamanını belirliyoruz
    bitis_zamani = datetime.now(timezone.utc) + timedelta(minutes=TOKEN_SURESI_DAKIKA)
    kopyalanacak_veri.update({"exp": bitis_zamani})

    # Sınırları belirlenmiş, mühürlenmiş Token'ı (VIP Kartı) bas!
    sifreli_token = jwt.encode(kopyalanacak_veri, SECRET_KEY, algorithm=ALGORITHM)
    return sifreli_token


# Swagger'daki o Kilit ikonunun (Authorize) çalışması için giriş kapısını gösteriyoruz
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="giris-yap")


# İŞTE GÜVENLİK GÖREVLİSİ (BOUNCER) BU FONKSİYON!
def token_dogrula(sifreli_token: str = Depends(oauth2_scheme)):
    try:
        # VIP kartı makineden geçir (Çöz)
        cozulmus_veri = jwt.decode(sifreli_token, SECRET_KEY, algorithms=[ALGORITHM])

        # Kartın kime ait olduğunu bul
        kimlik = cozulmus_veri.get("sub")
        if kimlik is None:
            raise HTTPException(status_code=401, detail="Geçersiz VIP Kart!")

        return kimlik  # Kimin giriş yaptığını döndür (Örn: "kral")

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401, detail="Bu kartın süresi dolmuş! (30 dk geçti)"
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401, detail="Sahte veya bozuk VIP Kart! Polisi arıyorum!"
        )
