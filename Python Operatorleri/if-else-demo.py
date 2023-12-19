# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme 
#    durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu 
#    lise ya da üniversite olmalıdır. 

# isim = input('isminiz: ')
# yas = int(input('yaşınız: '))
# egitim = input('eğitim: ')

# if yas >= 18:
#     if egitim == "lise" or egitim == "üniversite":
#         print ("ehliyet alabilirsiniz.")
#     else:
#         print ("eğitim durumunuzdan dolayı ehliyet alamazsınız.")
# else:
#     print ("18 yaş tamalamadığınızdan dolayı ehliyet alamazsınız.")


# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
#    not aralığına karşılık gelen not bilgisini yazdırınız.
#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5

# yazili1 = float(input('1.yazılı: '))
# yazili2 = float(input('2.yazılı: '))
# sozlu = float(input('sözlü: '))
# notunuz = 0
# ortalama = (yazili1 + yazili2 + sozlu) / 3

# if ortalama >=0  and ortalama < 24:
#     notunuz = 0
#     print (f"ortalamanız: {ortalama} ve notunuz: {notunuz}")
# elif ortalama >=25  and ortalama < 44:
#     notunuz = 1
#     print (f"ortalamanız: {ortalama} ve notunuz: {notunuz}")
# elif ortalama >=45  and ortalama < 54:
#     notunuz = 2
#     print (f"ortalamanız: {ortalama} ve notunuz: {notunuz}")
# elif ortalama >=55  and ortalama < 69:
#     notunuz = 3
#     print (f"ortalamanız: {ortalama} ve notunuz: {notunuz}")
# elif ortalama >=70  and ortalama < 84:
#     notunuz = 4
#     print (f"ortalamanız: {ortalama} ve notunuz: {notunuz}")
# elif ortalama >=85  and ortalama <= 100:
#     notunuz = 5
#     print (f"ortalamanız: {ortalama} ve notunuz: {notunuz}")
# else:
#     print ("Geçersiz not")





# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
#    göre hesaplayınız.
#    1. Bakım => 1. yıl     
#    2. Bakım => 2. yıl      
#    3. Bakım => 3. yıl     
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız..
#    *** datetime modülünü kullanmanız gerekiyor.  
#    (simdi) - (2018/8/1) => gün

import datetime
tarihGirisi = input ("aracınız trafiğe çıkış tarihini 'GG.AA.YYYY' formatında yazınız: ")

duzenliTarih = datetime.datetime.strptime (tarihGirisi, "%d.%m.%Y").date()
today = datetime.date.today()
print (f"Bugün: {today}")
print (f"Trafikten Çekiliş Tarihi: {duzenliTarih}")
fark = (today-duzenliTarih).days
print (fark)


if fark  <=365:
    print ("1. yıl bakımı")
elif fark > 365 and fark <=365*2:
    print ("2. yıl bakımı")
elif fark > 365*2 and fark <=365*3:
    print ("3. yıl bakımı")
else:
    print ("yanlış süre")
   