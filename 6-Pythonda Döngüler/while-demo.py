sayilar = [1,3,5,7,9,12,19,21]

# 1: sayilar listesini while ile ekrana yazdırın.

'''
x = 0
while x < len (sayilar):
    print (sayilar [x])
    x += 1
'''

# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm
#    tek sayıları ekrana yazdırın.
'''
x = int (input ("x: "))
y = int (input ("y: "))


while x < y:
    print (x)
    x+=1
'''

# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.


'''
x= 100
while x > 0:
    print (x)
    x-= 1
'''

# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde
#    yazdırın.

'''
numbers = []

x= 0
while x<5:
    number = int (input("sayi: "))
    numbers.append(number)
    x+=1

numbers.sort()
print (numbers)
'''


# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (name, price) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

'''
products = []

amount = int (input ("kaç ürün eklemek istiyorsunuz: "))
i = 0
while i < amount:
    products.append ({input (f"produc {i+1} name:  "):int (input ("price: "))})
    i+= 1

print (products)
'''

products = []

amount = int (input ("kaç ürün eklemek istiyorsunuz: "))
i = 0
while i < amount:
    name = input (f"produc {i+1} name: ")
    price = int (input ("price: "))
    products.append (
        {"name": name,
        "price": price})
    i+= 1

for product in products:
    print (f"product name: {product['name']}: product price {product['price']}")