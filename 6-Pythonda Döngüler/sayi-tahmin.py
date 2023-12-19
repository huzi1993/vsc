'''
   1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile
   buldurmaya çalışın. (hak = 5)
   ** "random modülü" için "python random" şeklinde arama yapın.
   ** 100 üzerinden puanlama yapın. Her soru 20 puan.
   ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı 
      üzerinden hesaplansın.
'''



# import random
# sayi = random.randint(1,10)

# hak = 5
# sayac = 0
# puan = 100


# while hak > 0:
#     hak -=1
#     sayac += 1
#     tahmin = int (input (f" {sayac}. Tahmininiz: ")) 
#     if tahmin == sayi:
#         print (f"Sayıyı {sayac}. defada bildiniz ve puanunuz: {puan}")

#         break
#     elif sayi > tahmin:
#         print ("yıkarı")
#     else:
#         print ("aşağı")
    
#     puan -= 20
    

#     if hak == 0:
#         print (f"Tahmin hakkınızı kaybettiniz. Tutulan sayı: {sayi}") 

# print (f"Tutulan sayı: {sayi}") 

import random
sayi = random.randint(1,10)


can = int (input("can hakkınız: "))
hak = can
sayac = 0
puan = 100



while hak > 0:
    hak -=1
    sayac += 1
    tahmin = int (input (f" {sayac}. Tahmininiz: ")) 
    if tahmin == sayi:
        print (f"Sayıyı {sayac} tahminle bildiniz ve puanunuz: {100- (100/can)* (sayac-1)}")

        break
    elif sayi > tahmin:
        print ("yıkarı")
    else:
        print ("aşağı")
    
    puan -= 20
    

    if hak == 0:
        print (f"Tahmin hakkınızı kaybettiniz. Tutulan sayı: {sayi}") 

print (f"Tutulan sayı: {sayi}") 