thislist = ["apple", "banana", "cherry"]
# print(thislist)


# allow duplicate value in list

thislist = ["apple", "banana", "cherry", "apple", "cherry"]

# print(thislist)

# list lenght

# print(len(thislist))

list1 = ["abc", 34, True, 40, "male"]

# print(type(list1))

# list counsturtor 
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)

# print(list1[0])
# print(list1[-1])
# print(list1[2:5])
# print(list1[:4])
# print(list1[2:])
# print(list1[-4:-1])

# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
# print(thislist)


thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)


thislist.insert(2, "sadsad")
# print(thislist)

thislist.append("orange")
# print(thislist)

thislist.insert(1, "redddddd")
# print(thislist)

tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
# print(thislist)


thislist.remove("apple")
# print(thislist)


thislist.pop(1)
# print(thislist)

thislist.pop()
# print(thislist)

del thislist[0]
# print(thislist)

thislist = ["apple", "banana", "cherry"]

# for loop 

# for x in thislist:
#   print(x)

# Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])


# //////////// List Comprehension ///////////////////////
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

# print(newlist)

newlist = [x for x in fruits ]
# print(newlist)

thislistOne = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislistOne.sort()
# print(thislistOne)


thislistTwo = [100, 50, 65, 82, 23]
thislistTwo.sort()
# print(thislistTwo)

thislistThree = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislistThree.sort(reverse = True)
# print(thislistThree)
thislistLast = ["apple", "banana", "cherry"]





















