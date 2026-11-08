while True:
    girdi = input("Lütfen bir sayı girin: ")

    if girdi.isdigit():
        print(f"Tebirkler girdiğiniz sayı: {girdi}")
        sayi = int(girdi)
        break
    else:
        print("Lütfen geçerli bir sayı girin.")