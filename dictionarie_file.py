thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
  }

# print(thisdict)

# print(thisdict["brand"])



# Duplicates Not Allowed
thisdictssss = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
# print(thisdictssss)
# print(len(thisdictssss))

thisdictssjsjsjsjs = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
# print(thisdictssjsjsjsjs)


# //////////////// Accessing Items ////
xasdaada= thisdict.get("model")
# print(xasdaada)

# ////////// Get Keys  /////////
xadasdad = thisdict.keys()

# print(xadasdad)


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

# print(x) #before the change

car["color"] = "white"

# print(x) #after the change


sadsadsax = thisdict.values()
# print(sadsadsax) 
xadsadad = thisdict.items()
# print(xadsadad) 


thisdictasdasda = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdictasdasda["year"] = 2018

# print(thisdictasdasda)

thisdictasdadsa = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdictasdadsa.update({"year": 2020})

# print(thisdictasdadsa)


# /////////////////// Adding Items ///////////////////
thisdictajsjsad = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdictajsjsad["color"] = "red"
# print(thisdictajsjsad)

# ////////////////// Update Dictionary ////////////////
thisdictasdsadad = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdictasdsadad.update({"color": "red"})

# print(thisdictasdsadad)

# ////////////////////////////// Removing Items   /////////////////////
thisdicasdsasat = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdicasdsasat.pop("model")
# print(thisdicasdsasat)

thisdict2131weqe= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# thisdict2131weqe.popitem()
# print(thisdict2131weqe)

# for x in thisdict2131weqe:
#   print(x)

# for x in thisdict2131weqe:
#   print(thisdict2131weqe[x])

# for x in thisdict2131weqe.values():
#   print(x)


# for x, y in thisdict2131weqe.items():
#   print(x, y)

# /////////////////////////// Copy a Dictionary ////////////////////

thisdict1231adads = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict1231adads.copy()
# print(mydict)

thisdict2131321qw221 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict2131321qw221)
# print(mydict)


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# print(myfamily)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamildassaady = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamildassaady)





























