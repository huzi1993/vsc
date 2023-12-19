from datetime import date
today = date.today ()

print (today)

day1 = date.fromisoformat ("2023-11-26")

print (day1)

myBirthday = date(today.year, 11, 26)
print (myBirthday)
asd = abs (today - day1)
print (asd.days)
