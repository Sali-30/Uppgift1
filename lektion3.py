#repetition om kap 1
#kapitel 2 
#strings

#str = "Hello"
#str[0] = "h" #man kan inte ändra sträng på det här sättet 

#str = "Hello"
#new_str = "h" + str[1:] #den här är det rätt sätt att ändra något i en string 
#print (new_str)

# str = "Python"
# new_str = str[:2] + "T" + str[3:] #en till exempel här ändrar man T för stora bokstav och : är för att alla nokstav ska va med. 
# print(new_str)

# age = 32 
# result = " i am " + str(age) + " years old" #har kan inte köra vara med "age"
# print(result)

# print('3' + '5')
# print(3 + 5)

# words = ["Hello", "World", "Python"]
# result = ":".join(words)
# print(result)

# str ="Hello World"
# print(str.upper())
# print(str.lower())

# str = "hello World"
# print(str.capitalize())
# print(str.title())

# str = " Hello World " #den här ska vi använda för att städa script 
# print(str)
# print(str.strip())

# str = " Hello World "
# print(str)
# print(str.strip())
# print(str.lstrip())
# print(str.rstrip())

# str = "apple,banan,cherry" #för listor 
# fruits = str.split(',')
# print(fruits)

# str = "one,two,three,four" #listor med variabel "str"
# str = str.split(',', 2)
# print(str)

# words = "I like apples"
# print(words.replace("apples", "melons")) #funktion för att remplazar apples för melon 

# words = "Hello World"
# print(words.find("World")) #för att hitta vad ordet befiner sig 

# Name = "Bobbo"
# age = 37
# print(f"My name is {Name} and I am {age}") #method för att lägga till allt i en string "f: formatering" 

#listor
# empty_list = []

# my_list = ["apple", 42, True, 3.14]
# print(my_list[1]) # det blir 42 för att 0 är apple

# my_list = ["apple", 42, True, 3.14]
# print(my_list[-1]) #man går bakåt, det atras para delante 

# my_list = ["apple", 42, True, 3.14]
# my_list[3] = "melon" #för att byta ut en dtatype i den har falet 3.14
# print(my_list)

# numbers = [1,2,3,4,5]
# numbers[1:4] = [20,30,40] #för att lägga till data i listan i en bestäm plats inne i listan 
# print(numbers)

# numbers = [1,2,3,4,5]
# numbers.append(6) #method för att addera data i sluten av listan 
# print(numbers)

# numbers = [1,2,3,4,5]
# numbers.insert(122, "hej") #för att insertar något 
# print(numbers)

# fruits = ["apple", "banana", "melon", "cherry"] #för att ta bort nofåt från listan
# fruits.remove("melon")
# print(fruits)

#fruits = ["apple", "banana", "melon", "cherry"]
# deleted = fruits.pop(2)
# print(f"we removed {deleted} in our list: {fruits}") #ta bor saker från listor .pop funktion 

# fruits.pop()
# print(fruits)

# del fruits #ta bort hela listan 
# print(fruits)

# fruits.clear() #för att ta bort allt inne i listan 
# print(fruits)

# fruits = ["apple", "banana", "melon", "cherry", "pear"]
# print(fruits[1:4])
# print(fruits[:3])
# print(fruits[2:])
# print(fruits[::2])
# print(fruits[::-1])
# print(fruits[-1:])

# fruits = ["apple", "banana", "melon", "cherry", "pear"]
# numbers = [7,2,4,1,5]
# numbers.sort()
# print(numbers)

# numbers = [7,2,4,1,5]
# print(sum(numbers))

#dictionaries i Python
#empty_dict = {} #vi kan ändra befintkiga värde eller lägga till värde 
#person = {"name": "Bobbo","age": 32, "city": "Linköping"}
#print(person["names"])
#print(person.get("proffession", "unknow"))
# person["proffesion"] = "hacker" #lägga till mer information 
# print(person)

# age = person.pop("age") #ta bort age - en key 
# print(age)
# print(person)

# del person["name"] # ta bort name 
# print(person)

# person["proffesion"] = "hacker"
# print(person)
# key, value = person.popitem() #ta bort senaste som har inlaggts 
# print(key, value)
# print(person )

#person = {"name": "Bobbo","age": 32, "city": "Linköping"}
#person.clear() # method för att städa listan 
#print(person)

# keys = person.keys()
# print(keys)

# values = person.values()
# print(values)

# tuples = person.items()
# print(tuples)

##TUPLES##

# empty_tuple = ()
# small_tuple = (5,) #för att lägga till värde måste man skriva kommatecken , 

#fruits = ("apple", "melon", "cherry")

# fruits = "apple", "melon", "cherry"
# print(fruits)
# print(type(fruits)) #den ahr funktionalitet visar vilken klass tillhör fruits 

# fruits = ("apple", "melon", "cherry")
# print(fruits[0])
# print(fruits[-1])

# print(fruits[1:4])
# fruits[1] = "banana"

# fruits = ("apple", "melon", "cherry")
# fruits_list = list(fruits)
# fruits_list[1] = "banana"
# fruits = tuple(fruits_list)
# print(fruits)

# fruits = ("apple", "melon", "cherry")
# fruit1, fruit2, fruit3 = fruits
# print(fruit1)
# print(fruit2)
# print(fruit3)

# fruits = ("apple", "melon", "banana", "cherry")
# # fruit1, fruit2, *rest = fruits
# # print(fruit1)
# # print(fruit2)
# # print(rest)

# numbers = fruits.count("melon")
# print(numbers)

##SETS## 

empty_set = set()
fruits = {"apple", "banana", "cgerry", "apple"}
# print(fruits)
# print(fruits[0])

# fruits.add("grape") #lägger till fler element från em lista 
# print(fruits)

# fruits.update(["orange", "mango"])
# fruits.remove("banana") #finns inte banana i listan 
# print(fruits)

# fruits.discard("cherrys")
# print(fruits)

# element = fruits.pop()
# print(element)
# print(fruits)

# fruits.clear()
# print(fruits)

set1 = {1,2,3}
set2 = {3,4,5}

# union_set = set1 | set2 #para unir los set
# union_set = set1.union(set2)
# print(union_set)

# intersection_set = set1 & set2
# print(intersection_set)

# diffrence_set = set1 - set2
# print(diffrence_set)

# symmetric = set1 ^ set2
# print(symmetric)

# frozen_fruits = frozenset(["apple", "orange", "grape"])
# print(frozen_fruits)

# frozen_fruits.add("banana")
# print(frozen_fruits)