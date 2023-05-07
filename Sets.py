'''
-> Sets = Set is similar to dictonary but sets are immutable and doesn't have repetative file 


a = {} it will create an empty dictonary 
a = set() it will create an empty set
'''

a ={1,3,4,5,1}
print(a) #doesn't allow repetative items
print(type(a))



b = set()
print(b)
b.add(4)
b.add(3)
b.add(3)
b.add(5)
b.add(5)
print(b)
#b.add({4:5}) # cannot add list or dictonary to sets

print(len(b))


print(b.pop()) #remove a random value  element and return set
b.remove(4)
print(b) #removes the value 3 from the set 
print(b.clear()) #empties the set 
print(b.union({8,11})) #returns a new set which contains only items in both sets
print(b.intersection({8,11}))  # returns a set which contains only items in both sets {8}

