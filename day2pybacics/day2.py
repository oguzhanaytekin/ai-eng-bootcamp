liste = []
while True:
    i_girdi = input("isim giriniz (q for exit):")
    if i_girdi.lower() == "q":

        break

    v_girdi = input("vize not giriniz :")
    vize = int(v_girdi)

    f_girdi = input("final not giriniz:")
    final = int(f_girdi)

    avg = float(0.4 * vize + 0.6 * final)

    if avg < 50:
        decider = "Kaldiniz"
    elif avg >= 50 and avg < 85:
        decider = "Gectiniz"
    else:
        decider = "Tebrikler(AA)"

    ogrenci = {
        "İsim": i_girdi,
        "Vize Notu": vize,
        "Final Notu": final,
        "Ortalama": avg,
        "Gectiniz/Kaldiniz/Tebrikler": decider,
    }

    liste.append(ogrenci)
    print(f"{liste}")

tumnotlar = [ogr["Ortalama"] for ogr in liste]

toplam_tum = sum(tumnotlar)

avg_sinif = sum(tumnotlar) / len(liste)

print(f"Sinif Ortalamasi: {avg_sinif}")


""" Kodları inceledim. Gözlerimden yaş geldi desem yeridir... Çünkü sabahki o spagetti kod gitmiş, yerine "Mühendis" mantığıyla yazılmış, temiz bir yapı gelmiş.

Operasyon Başarılı. Temel algoritma mantığını, liste yönetimini ve döngüleri kavramışsın.

Ama madem "realist ol, eleştir" dedin; o zaman kodunu bir Senior Mühendis gözüyle "Code Review" (Kod İncelemesi) masasına yatıralım.

Neleri Geliştirebilirdik? (Teknik Analiz)
1. "Patlama" Riski (Division by Zero Error): Kodunu çalıştırıp, hiç öğrenci girmeden direkt q tuşuna basarsan ne olur?

liste boş kalır (len(liste) = 0 olur).

En altta sum / len yaparken, sayıyı 0'a bölmeye çalışırsın.

Python sana küfür eder: ZeroDivisionError.

Çözüm: En son hesaplamayı if len(liste) > 0: içine alman lazımdı. (Bunu bir önceki mesajda örnekte vermiştim, gözden kaçmış ama canın sağ olsun).

2. Gereksiz İşlem (Redundancy): Şu kısma bak:

Python

toplam_tum = sum(tumnotlar)  # Burada topladın, değişkene attın.
avg_sinif = sum(tumnotlar) / len(liste) # Burada değişkendeki hazır değeri kullanmak yerine TEKRAR toplattın.
Bilgisayar yorulmaz ama büyük veride bu hatadır. Doğrusu: avg_sinif = toplam_tum / len(liste) olmalıydı.

3. "Kullanıcı Aptaldır" İlkesi (Input Validation): Sen kullanıcıya "Not gir" dedin. Kullanıcı "90" yerine yanlışlıkla "doksan" yazarsa ne olur?

int("doksan") satırı kodu patlatır (ValueError).

Gelecek Derslerin Konusu: İleride bunu try-except bloklarıyla korumaya alacağız. Şimdilik bilmen yeterli. """
