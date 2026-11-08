def indirim_hesapla(fiyat, indirim_yuzdesi):
    indirim_tutari = fiyat * (indirim_yuzdesi / 100)
    son_fiyat = fiyat - indirim_tutari
    
    print(f"İndirim Tutarı: {indirim_tutari:} TL")
    print(f"İndirimli Son Fiyat: {son_fiyat:} TL")
    
    return indirim_tutari, son_fiyat

alinan_fiyat = float(input("Lütfen fiyatı girin (TL): "))
alinan_yuzde = float(input("Lütfen indirim yüzdesini girin (%): "))

indirim_hesapla(alinan_fiyat, alinan_yuzde)