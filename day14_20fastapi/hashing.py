import bcrypt


class Hash:
    @staticmethod
    def bcrypt(password: str):
        # 1. Düz şifreyi byte formatına çevir
        password_bytes = password.encode("utf-8")

        # 2. Şifreyi "tuzla" (salt) ve karmaşıklaştır
        hashed_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

        # 3. Veritabanına metin (TEXT) olarak yazabilmek için tekrar string'e çevir
        return hashed_bytes.decode("utf-8")

    @staticmethod
    def verify(hashed_password: str, plain_password: str):
        # Girilen şifre ile veritabanındaki karmaşık şifre uyuşuyor mu diye kontrol et
        return bcrypt.checkpw(
            plain_password.encode("utf-8"), hashed_password.encode("utf-8")
        )
