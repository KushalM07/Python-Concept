'''
-> Tupples =  Containers to store a set of values of any data types but it can't be updated ie immutable

t = (1,2 ,3,4,5)
print(t[0])
output = 1

t[0] = 34
print(t[0])
it will throw an error 


t1 =() -> empty tupple and if you ever enter a single value in tupple just add comma (,) 
'''
#wrong way
t1 = (1);
print(t1)
print(type(t1))
#right way
t2 = (1,)
print(t2)
print(type(t2))



#creating a Tupple
t = (1,2,4,5,4)
print(t.count(1))  #return the number of occurence of value 
print(t.index(1)) # return the index of given value 


