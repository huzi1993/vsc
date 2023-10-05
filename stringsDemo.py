website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?
result = len(course)
length = len (website)

# 2- 'website' içinden www karakterlerini alın.
result = website [7:10]


# 3- 'website' içinden com karakterlerini alın.

result = website [22:25]
result = website [length-3:length]



# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
result = course [:15]
lenCourse = len(course)
result = course [0:15] + " - " + course [lenCourse-15:lenCourse]
result = course [0:15] + " - " + course [-15:]
# 5- 'course' ifadesindeki karakterleri tersten yazdırın.

result = course [::-1]
name, surname, age, job = "Huzeyfe","Muhammed", 30, "Tercüman" 

# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    "Benim adım Huzeyfe Muhammed, Yaşım 32 ve mesleğim Tercüman." 

result = f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}"
result = "Benim adım " + name  + " " + surname + ", yaşım " + str(age) + " ve mesleğim " +job
result = "Benim adım {} {}, yaşım {} ve mesleğim {}".format (name, surname, age, job)


# 7- "Hello world" ifadesindeki w harfini "W" ile değiştirin.


stringim = "Hello world"
stringim = stringim[0:6] + "W" + stringim[-4:]
stringim.replace("w","W")
# print (stringim)

# 8- "abc" ifadesini yan yana 3 defa yazdırın.
abc = "abc "
result = abc * 3

print (result)