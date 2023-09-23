maasAli = 5000
maasAhmed = 4000
vergi = 0.27

print (maasAli - (maasAli*vergi))
print (maasAhmed - (maasAhmed*vergi))

# Değişken tanımlama kuralları:
# rakam ile başlayamaz
# ona değer atmalıyız
# aynı değişken ismini iki kez kullanımamalı

number1 = 10
print(number1)

number1 = 20
print(number1)

number1 += 30
print(number1)

# Büyük küçük harf duyarlılığı

age = 12
AGE = 100

print("age: " + str(age))
print("AGE: " + str(AGE))

# Türkçe karakter kullanmayalım
# Boşluk burakılmaz

yas = 20
_age = 20

x = 1              # int
y = 2.3            # float 
name = "Çınar"     # string
isStudent = True   # bool

# x, y, name, isStudent = (1, 2.3, "Çınar", True)

a = '10'
b = '20'
print(a+b) # => 1020

firstName = "Huzeyfe"
lastName = " Muhammed"

print(firstName + lastName)  # Huzeyfe Muhammed