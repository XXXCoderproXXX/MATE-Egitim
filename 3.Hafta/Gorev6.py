from datetime import datetime

def vize_sayaci():

    while True:
        tarih_str = input("Lütfen vize tarihini ve saatinizi girin (Örn: 15.11.2026 14:30): ")
    
        try:
            sinav_zamani = datetime.strptime(tarih_str, "%d.%m.%Y %H:%M")
            su_an = datetime.now()
        
            kalan_sure = sinav_zamani - su_an
        
            if kalan_sure.total_seconds() < 0:
                print("Bu sınavın tarihi çoktan geçmiş!")
            else:
                gun = kalan_sure.days
                saat = kalan_sure.seconds // 3600 - 3
                print(f"Sınavınıza tam olarak {gun} gün, {saat} saat kaldı. Başarılar!")

            break
            
        except ValueError:
            print("Hatalı format! Lütfen tarihi 'GG.AA.YYYY SS:DD' formatında girdiğinizden emin olun.")

vize_sayaci()