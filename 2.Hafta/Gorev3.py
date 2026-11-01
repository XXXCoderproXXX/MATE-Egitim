dogum_yili = int(input("Doğum yılınızı girin: "))
yas = 2026 - dogum_yili

print(f"Yaşınız: {yas}")

if yas >= 18:
    print("Ehliyet alabilirsiniz.")
else:
    print("Ehliyet almak için yaşınız yeterli değil.")