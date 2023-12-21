thistuple = ("apple", "banana", "cherry")
# print(thistuple)

thistupleTwo = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistupleTwo)
# print(len(thistupleTwo))

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

thistuplethree = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuplethree)

# /////////////////// Access Tuple Items //////////////////

thistuple11 = ("apple", "banana", "cherry")
# print(thistuple11[1])
# print(thistuple11[-1])

# ////// Range of Indexes ////
thistuple22 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple22[2:5])
# print(thistuple22[:4])
# print(thistuple22[2:])


thistuple33 = ("apple", "banana", "cherry")
# if "apple" in thistuple33:
#   print("Yes, 'apple' is in the fruits tuple")
# else:
#   print("Yes, 'apple' is not in  the fruits tuple")
  

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

# print(x)

thistuple44 = ("apple", "banana", "cherry")
y = list(thistuple44)
y.append("orange")
thistuple44 = tuple(y)
# print(thistuple44)

ysss = ("orange",)
thistuple44 += ysss

# print(thistuple44)

# /////////////////////// Unpack Tuples /////////////////////////
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

thistuplsssse = ("apple", "banana", "cherry")
# for x in thistuplsssse:
#   print(x)


thistuplssssaaae = ("apple", "banana", "cherry")
# for i in range(len(thistuplssssaaae)):
#   print(thistuplssssaaae[i])

tupleqaaa1 = ("a", "b" , "c")
tupleaaaa2 = (1, 2, 3)

tuple3dadasda = tupleqaaa1 + tupleaaaa2
# print(tuple3dadasda)

fruitsaSAASSAs = ("apple", "banana", "cherry")
mytuple = fruitsaSAASSAs * 2

# print(mytuple)

# //////////////// Tuple count() Method ////////////////////
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(3)

# print(x)


# ////////////////////////// Tuple index() Method ///////////////////
thistupleasaasda = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistupleasaasda.index(8)

# print(x)












