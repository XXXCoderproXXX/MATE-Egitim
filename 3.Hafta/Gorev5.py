import random
import time
def sayi_tahmin_oyunu():
    print("Sayı Tahmin Oyununa Hoş Geldiniz!")
    print("7 tahmin hakkınız var. Doğru sayıyı bulabilecek misiniz?")
    
    gizli_sayi = random.randint(1, 100)
    tahmin_hakki = 10

    while tahmin_hakki > 0:
        tahmin = input("1 ile 100 arasında bir sayı tahmin edin: ")

        if tahmin.isdigit():
            tahmin = int(tahmin)

            if tahmin < 1 or tahmin > 100:
                print("Lütfen 1 ile 100 arasında bir sayı girin.")
                continue

            if tahmin < gizli_sayi:
                print("Daha yüksek bir sayı deneyin.")
                time.sleep(1)
                tahmin_hakki -= 1

            elif tahmin > gizli_sayi:
                print("Daha düşük bir sayı deneyin.")
                time.sleep(1)
                tahmin_hakki -= 1

            else:
                print(f"Tebrikler! Doğru sayıyı buldunuz: {gizli_sayi}")
                time.sleep(1)
                break

            print(f"Kalan tahmin hakkınız: {tahmin_hakki}")

        else:
            print("Lütfen geçerli bir sayı girin.")
    if tahmin_hakki == 0:
        print(f"Üzgünüz, tahmin hakkınız bitti. Doğru sayı: {gizli_sayi}")

sayi_tahmin_oyunu()