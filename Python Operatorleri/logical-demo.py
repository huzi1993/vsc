
# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

# x = float ( input ("x: "))

# if x > 0 and x < 100:
#     print (f"girilen sayı {x}, ve bu sayı 0-100 arasındadır")
# else:
#     print (f"girilen sayı {x}, ve bu sayı 0-100 arasında değildir")



# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

# x = int ( input ("x: "))

# if x > 0:
#     if x %2 == 0:
#         print ("girilen sayı pozitif çift sayı")
#     else:
#         print ("girilen sayı pozitif tek sayı")

# else:
#     print ("girilen sayı pozitif değildir")


# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.


# mail = "alikomdotcom@ggg.com"
# password = "asd123"

# eMail = input ("Mail adresinizi giriniz: ")
# parola = input ("parolanızı giriniz: ")

# if eMail == mail:
#     if parola == password:
#         print ("Girilen bilgiler doğru")
#     else:
#         print ("Girilen parola yanlış")    
# else:
#     print ("girilen mail adresi yanlış")



# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.


# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))
# enBuyuk = a


# if  b > a and b > c:
#     enBuyuk = b
# elif  c > a and c > b:
#     enBuyuk = c
# print (f"En büyük sayı: {enBuyuk}")

# if  a > b and a > c:
#     print ("A en büyük sayıdır")
# elif  b > a and b > c:
#     print ("B en büyük sayıdır")
# elif  c > a and c > b:
#     print ("C en büyük sayıdır")


# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.


# vize1 = float (input("vize1: "))
# vize2 = float (input("vize2: "))
# final = float (input("final: "))
# mean =  (((vize1 + vize2)/2)*0.6)+(final*0.4)


#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.


# if mean>=50:
#     if final >=50:
#         print (f" Öğrenci ortalaması: {mean} ve geçme durumu: başarılı")
#     else:
#         print (f" Öğrenci ortalaması: {mean} ve geçme durumu: başarısız. final notu 50den fazla olamalı")
# else:
#     print (f" Öğrenci ortalaması: {mean} ve geçme durumu: başarısız")


#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.


# if mean>=50:
#     print (f" Öğrenci ortalaması: {mean} ve geçme durumu: başarılı")
# else:
#     if final >= 70:
#         print (f" Öğrenci ortalaması: {mean} ve geçme durumu: başarılı. Finalde 70 üsütü aldığınınz için geçtiniz")
#     else:
#         print (f" Öğrenci ortalaması: {mean} ve geçme durumu: başarısız")


# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf
#    18.5-24.9 => Normal
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)


name = input ("Adınız: ")
kilo = float(input ("Kilonuz: "))
boy = float(input ("Boyunuz: "))
index = (kilo) / (boy **2)
obezDurumu = ""

if index > 0 and index <= 35:
    if index > 0 and index <= 18.4:
        obezDurumu = "Zayıf"
    elif index >= 18.5 and index <= 24.9:
        obezDurumu = "Normal"
    elif index >= 25.0 and index <= 29.9:
        obezDurumu = "Kilolu"
    elif index >= 30.0 and index <= 34.9:
        obezDurumu = "Şişman (Obez)"
    print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen obez durumunuz: {obezDurumu}')
else:
    print("Girdiniz bilgiler yanlıştır.")

