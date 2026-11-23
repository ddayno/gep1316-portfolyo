
from datetime import datetime

# Kullanıcının adını alıyoruz.
ad = input("Adınız nedir? ")

# Kullanıcının doğum yılını alıyoruz.
dogum_yili = int(input("Doğum yılınız nedir? "))

# Güncel yılı öğreniyoruz.
guncel_yil = datetime.now().year

# Doğum yılının geçerli olup olmadığını kontrol ediyoruz.
if dogum_yili > guncel_yil:
    print("Hata! Doğum yılı gelecekte olamaz.")

elif dogum_yili < 1900:
    print("Hata! Lütfen geçerli bir doğum yılı girin.")

else:
    # Kullanıcının yaklaşık yaşını hesaplıyoruz.
    yas = guncel_yil - dogum_yili

    # Kullanıcıya özel mesaj gösteriyoruz.
    print(f"Merhaba {ad}!")
    print(f"Yaklaşık {yas} yaşındasın.")
    print("GEP1316 Kodlama Okuryazarlığı dersine hoş geldin!")
