'''
-> List = Containers to store a set of values of any data types and it can be updated mutable
   
     Friends  = ['Apple' , 'Akash' , 'rohan' , 7 , False]

'''

a = [1,2,4,56,6]
print(a)
print(a[0])
a[0] = 98
print(a)   # value changed
# index starts from 0 till end 


#create a list with diff data types 
 
b= ['Kushal' , 234, False ,3.45 ,'']
print(b);

#List Slicing
Friends = ["harry" , 'Tom' ,'Rohan' ,45 , 'sam'  , 'divya']
print(Friends[0:4])
print(Friends[:4])
print(Friends[0::2])


#List methods *** very important
 
L1 =[1,8, 7, 2 , 21 ,15]
#remember it will change the original list 
L1.sort() 
print (L1);
print (L1.reverse()); # it will None  , So never do it like this 

L1.append(12)
print (L1);
L1.insert(4, 234)
print(L1)

L1.pop(2) #it will delete element at index 2 and return its value 
L1.remove(11) # it will remove this element if present else give error   



