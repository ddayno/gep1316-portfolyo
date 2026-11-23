
# Oyun Geliştirme Bütçe ve Kâr Hesaplayıcısı

# Kullanıcıdan oyun bilgilerini alıyoruz.
oyun_adi = input("Oyunun adını girin: ")

# Geliştirme bütçesini öğreniyoruz.
butce = float(input("Geliştirme bütçesi ($): "))

# Oyunun satış fiyatını öğreniyoruz.
fiyat = float(input("Oyunun satış fiyatı ($): "))

# Satılan kopya sayısını öğreniyoruz.
satis = int(input("Satılan oyun sayısı: "))

# Platform komisyon oranını belirliyoruz.
komisyon = 0.30

# Girilen değerlerin geçerli olup olmadığını kontrol ediyoruz.
if butce < 0 or fiyat < 0 or satis < 0:
    print("Hata! Negatif değer giremezsiniz.")

else:
    # Toplam satış gelirini hesaplıyoruz.
    brut_gelir = fiyat * satis

    # Platformun aldığı komisyonu hesaplıyoruz.
    komisyon_tutari = brut_gelir * komisyon

    # Komisyon sonrası geliri hesaplıyoruz.
    net_gelir = brut_gelir - komisyon_tutari

    # Geliştirme bütçesini çıkararak kârı buluyoruz.
    kar = net_gelir - butce

    # Oyunun kâr edip etmediğini kontrol ediyoruz.
    karli_mi = kar > 0

    # Sonuçları ekrana yazdırıyoruz.
    print(f"\nOyun: {oyun_adi}")
    print(f"Brüt gelir: ${brut_gelir:.2f}")
    print(f"Platform komisyonu: ${komisyon_tutari:.2f}")
    print(f"Komisyon sonrası gelir: ${net_gelir:.2f}")
    print(f"Kâr/Zarar: ${kar:.2f}")

    if karli_mi:
        print("Sonuç: Oyun kâr etti!")
    elif kar == 0:
        print("Sonuç: Oyun başa baş!")
    else:
        print("Sonuç: Oyun zarar etti!")
