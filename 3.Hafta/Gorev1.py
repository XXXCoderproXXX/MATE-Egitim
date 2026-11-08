import time
def geri_sayim(sayi):
    while sayi >= 0:
        print(sayi)
        sayi -= 1
        time.sleep(1)

girilen_sayi = int(input("Lütfen bir sayı girin: "))
print("Geri sayım başlıyor...")
geri_sayim(girilen_sayi)