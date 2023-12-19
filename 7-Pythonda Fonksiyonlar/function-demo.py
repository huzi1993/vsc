# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın. 

# def yazdir (sayi , kelime):
#     i = 0
#     while i < sayi:
#         print (kelime)
#         i+= 1
    

# kelime = input  ("yazdırmak istediğiniz kelimeyi yazınız: ")
# tekrarSayisi = int (input("tekar sayısı giriniz: "))

# yazdir (tekrarSayisi, kelime)


# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.

# def tekrarListesi(*params):
#     liste = []

#     for param in params:
#         liste.append(param)

#     return liste

# result = tekrarListesi(10,20,30,"alo")

# print(result)


# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.


def asalaSayiler (sayi1, sayi2):
    for sayi in range (sayi1, sayi2+1):
        if sayi > 1:
            for i in range (2, sayi):
                if sayi % i== 0:
                    break
            else:
                print (sayi)
        
sayi1 = int (input ("Sayi 1 = "))
sayi2 = int (input ("Sayi 2 = "))

asalaSayiler (sayi1, sayi2)


# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz.



# def tamBolen (sayi):
#     tamBolenler = []
#     for i in range (1,sayi):
#         if sayi % i ==0:
#             tamBolenler.append(i)
#     return tamBolenler

# sayi = int (input ("Sayı= "))

# print (tamBolen(sayi))
 











# def tamBolenleriBul(sayi):
#     tamBolenler = []

#     for i in range(2, sayi):
#         if (sayi % i == 0):
#             tamBolenler.append(i)
    
#     return tamBolenler


# print(tamBolenleriBul(100))