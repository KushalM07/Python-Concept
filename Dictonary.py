'''
-> Dictonary is a collection of key -value pairs 
-> properties of dictornaries
  - it is unordered
  - it is mutable 
  - it is indexed
  - cannot contain duplicate key
  - O(1) time 
Syntax 
 a = {"key" : "value",
      "harry" : "code",
      ...
      ....
      so on
      }
'''

myDict ={
    'Fast' : 'in a quick Manner',
    'harry':'A Coder',
    'Marks':[1,2,5],
    'AnotherDict':{'Harry':'Player'}
}
print(myDict['Fast'])
print(myDict['Marks'])
print(myDict['AnotherDict']['Harry'])

#changing the value 
myDict['Marks'] = [45,78]
print(myDict['Marks'])


# Mehods in Dict 

MyDict ={
    'fast' : 'in a quick Manner',
    'name':'Kushal',
    'marks':[1,2,5],
    'anotherDict':{'type':'Player'}
}

print(MyDict.keys()) #print all the keys of the dictonary   
print(MyDict.values()) #print all the values of the dictonary
print(MyDict.items()) #gives items in the form of a list and we can iterate through it 
updateDict ={
    'lovish':'friend'   
}
MyDict.update(updateDict) #updates the dictonary by adding key-values pair from updateDict 
print(MyDict)


print(MyDict['name'])
print(MyDict.get('name'))
'''  
 difference between them as the output of them is same 
 so the answer is 
 if we put 
 print(MyDict.get('name2'))
 although it doesn't exist but still it will be not throw  an error  just return "None" 
 '''