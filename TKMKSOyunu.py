# Bilgisayarla karşılıklı oynanacağı için bilgisayarın random sayı üretmesi gerekir.
# Bu yüzden random kütüphanesi import edilir.
import random

# Bilgisayarın üreteceği random sayılara karşılık gelen terimler için aşağıdaki fonksiyon yazılır.
def sayi_donusum_isim(sayi):
  if sayi == 0:
    return "Taş"
  elif sayi == 1:
    return "Spock"
  elif sayi == 2:
    return "Kağıt"
  elif sayi == 3:
    return "Kertenkele"
  elif sayi == 4:
    return "Makas"
  else:
    return "Hata"

# Oyuncunun gireceği terime karşılık sayılara dönüşüm yapılır. (Gerekli hesaplamaların yapılması amaçlı)
def isim_donusum_sayi(isim):
  if isim == "Taş":
    return 0
  elif isim == "Spock":
    return 1
  elif isim == "Kağıt":
    return 2
  elif isim == "Kertenkele":
    return 3
  elif isim == "Makas":
    return 4
  else:
    print(isim + " Taş, Kağıt, Makas, Kertenkele, Spock karakterlerine dahil değil.")

# 10 kez doğru bilen kazanacağı için oyuncu ve bilgisayar kazanma sayıları tutulur.
oyuncu_kazanma_sayisi = 0
bilgisayar_kazanma_sayisi = 0
while oyuncu_kazanma_sayisi!=10 and bilgisayar_kazanma_sayisi!=10:
  tahmin = input("Seçiminizi giriniz..Seçenekler: Taş, Spock, Kağıt, Kertenkele, Makas" + "\n")

  # Oyuncudan alınan tercih karşılığı gelen sayıya dönüştürülür.
  oyuncu_sayisi = isim_donusum_sayi(tahmin)

  # Random fonksiyonu kullanılarak bilgisayarın tercihi random atanır.
  bilgisayar_sayisi = random.randrange(0,5)

  # Oyuncu sayısı ile bilgisayar sayısının farkı alınarak mod 5'i alınır.
  kazanan = (bilgisayar_sayisi - oyuncu_sayisi) % 5

  # Yapılan işlem sonucunda winner 3'ten küçükse bilgisayar kazanır oyuncu kaybeder
  if kazanan < 3:
     oyuncu_kazanan = False
  else:
     oyuncu_kazanan = True

  # Bilgisayar sayısı oluşturulan fonksiyon kullanılarak bilgisayarın seçtiği tercih ismine dönüştürülür
  bilgisayar_secimi = sayi_donusum_isim(bilgisayar_sayisi)

  # Sonuçlar yazdırılır 
  print("Oyuncu seçimi: " + tahmin)
  print("Bilgisayar seçimi: " + bilgisayar_secimi)
  if oyuncu_kazanan:
    oyuncu_kazanma_sayisi += 1
    print("Oyuncunun " + str(oyuncu_kazanma_sayisi) + ". galip gelişi!\n")
  elif bilgisayar_sayisi == oyuncu_sayisi:
    print("Oyuncu ve bilgisayar berabere!\n")
  else:
    bilgisayar_kazanma_sayisi += 1
    print("Bilgisayarın " + str(bilgisayar_kazanma_sayisi) + ". galip gelişi!\n")

if oyuncu_kazanma_sayisi == 10:
  print("Oyun sonucunda OYUNCU KAZANDII!!")

elif bilgisayar_kazanma_sayisi == 10:
  print("Oyun sonucunda BİLGİSAYAR KAZANDII!")