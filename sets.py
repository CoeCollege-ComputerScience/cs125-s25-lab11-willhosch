set1 = set("abcdefg")
set2 = set("adegjke")
set3 = set("aaaaaaa")
#print(len(set1))
#Sets are mutable
#print(set1.append("h"))  # AttributeError: 'set' object has no attribute 'append'
#Sets can't be indexed because they are unordered
#Sets are iterable
#You can determine length of a set
#print ("a" in set1)
#You can determine if an element is in a set
#print (set1.pop())
#Removes a random element from the set and returns it
#set1 = set1.remove("a")
#Adds an element to the set
#print(set1)
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
print(set1)
