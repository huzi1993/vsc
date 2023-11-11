fruits = { "portakal", "elma", "muz"}

# print(fruits[0]) indekslenemez

for x in fruits:
    print(x)

fruits.add("çilek")
fruits.update(["mango","grifort","elma"])

fruits.remove("mango")
fruits.discard("elma")
fruits.pop()

fruits.clear()

print(fruits)

# myList = [1,2,5,4,4,2,1]
# print(myList)
# print(set(myList))