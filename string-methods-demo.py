website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"


# 1-  ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

result = " Hello World ".strip()
result = " Hello World ".lstrip()
result = " Hello World ".rstrip()

result = website.lstrip("htp:/")


# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.

result = "www.sadikturan.com".strip("w.com")


# 3-  'course' karakter dizisinin tüm karakterlerini küçük harf yapın.

result = course.lower()
result = course.upper()
result = course.title()


# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))

result = website.count ("a")
result = website.count ("www")
result = website.count ("www",0,1)



# 5- 'website' "www" ile başlayıp com ile bitiyor mu?

result = website.startswith ("www")
result = website.endswith ("com")

# 6-  'website' içinde '.com' ifadesi var mı?

result = website.find(".com")
result = website.find(".com",0,1)
result = course.find("Python")
result = course.rfind("Python")

result = website.index ("com")
result = website.rindex ("com")
#result = website.index ("comm")



# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)

result = course.isalpha()
result = "alpha".isalpha()
result = "132".isdigit()

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.

result = "Contents".center(50)
result = "Contents".center(50, "*")
result = "Contents".ljust(50, "*")
result = "Contents".rjust(50, "*")



# 9-  'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.

result = course.replace(" ", "-")
result = course.replace(" ", "-", 5)
result = course.replace(" ", "")


# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin

result = "Hello World".replace("World", "There")

# 11-  'course' karakter dizisini boşluk karakterlerinden ayırın.

result = course.split(" ")
result = result [2]

print(result)
