a = 43
b = 'harry'

# print(a , b); 43 harry 
# print(type(a)) integer
# print(type(b)) String 
greeting  = "Good morning , "
name = "harry"
print(greeting + name) 
# Good morning harry

#Slicing the String

'''

name[startind : endind ] 
startind = included 
endind = not included







name[startind : endind : skip the chrarcter] 

skip the character  = this include this much character will be skipped 

'''
tobeSliced = "thisisKushal"
#print(tobeSliced[9])


# last character will not be included  'thi' 
print(tobeSliced[0:3])   
print(tobeSliced[:4]) 
print(tobeSliced[0:-1]) 
print(tobeSliced[0:]) 


''' 
output

thi
this
thisisKusha
thisisKushal

'''

print(tobeSliced[0::2])


