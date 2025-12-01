import json
import os
from day3_func import *


def load_veriler():
    if os.path.exists("ogrenciler.json"):
        with open("ogrenciler.json", "r", encoding="utf-8") as dosya:
            return json.load(dosya)
    else:

        return (
            []
        )  # eğer ogrenciler.json dosyası varsa oku listeyi döndür yoksa boş liste döndür.


def save_veriler(liste):
    with open("ogrenciler.json", "w", encoding="utf-8") as dosya:
        json.dump(liste, dosya, indent=4)
    print("veriler basariyla kaydedildi..")
