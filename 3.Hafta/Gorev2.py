def sayi_toplama(sayi):
    toplam = 0
    for i in range(1, sayi + 1):
        toplam += i
    return toplam
girilen_sayi = int(input("Lütfen bir sayı girin: "))
toplam_sonucu = sayi_toplama(girilen_sayi)
print(f"1'den {girilen_sayi} sayısına kadar olan sayıların toplamı: {toplam_sonucu}")