def harf_notu_hesapla(vize, final):
    ortalama = (vize * 0.40) + (final * 0.60)
    
    if ortalama >= 90:
        harf = "AA"
    elif ortalama >= 85:
        harf = "BA"
    elif ortalama >= 80:
        harf = "BB"
    elif ortalama >= 75:
        harf = "CB"
    elif ortalama >= 65:
        harf = "CC"
    elif ortalama >= 55:
        harf = "DC"
    elif ortalama >= 50:
        harf = "DD"
    else:
        harf = "FF"
        
    print(f"Ortalamanız: {ortalama:.2f}, Harf Notunuz: {harf}")
    return ortalama, harf

# Kullanıcıdan vize ve final notları alınıyor
alinan_vize = float(input("Lütfen vize notunuzu girin: "))
alinan_final = float(input("Lütfen final notunuzu girin: "))

# Fonksiyon, kullanıcının girdiği notlar ile çalıştırılıyor
harf_notu_hesapla(alinan_vize, alinan_final)