import time
def geri_sayim(sayi):
    print("Geri sayım başlıyor...")
    while sayi >= 0:
        print(sayi)
        sayi -= 1
        time.sleep(1)

girilen_sayi = int(input("Lütfen bir sayı girin: "))
geri_sayim(girilen_sayi)
print("Ateşle!")
