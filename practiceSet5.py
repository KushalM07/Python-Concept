'''
-> WAP to create a dict.. of hindi words with values as their english translation provide user with an option to look it up
-> WAP to input 5 numbers from the users and display all the unique numbers
-> Can we have a set with 18(int) and 18(str) as a value in it 
-> length of the following set 
  s=set()
  s.add(20)
  s.add(20.0)
  s.add("20") ->length of S after these operations 
  -> s ={}
  what is the type of S; 
  -? create an empty dict  , allow 4 frnds to enter their fvt lang. as values and use keys as thier name . Assume that the names are unique 
  -> if Name of  2 frnds are same what will you use dict or sets 
  
'''

#sols 1 
dict ={
    'Hello' : 'Jai Shree Ram',
    'fan' : 'Pankha',
    'Item' : 'Vastu'
}
print("Options are " , dict.keys())
a  = input("enter the English word \n")
#print("this meaning of your words is", dict[a]); #it will gives us error to prevent it we use 

print("the meaning of your word is", dict.get(a)) #it will not throw an error 


#sols 2

Numb1 = int(input("enter you num 1 \n"))
Numb2 = int(input("enter you num 2 \n"))
Numb3 = int(input("enter you num 3 \n"))
Numb4 = int(input("enter you num 4 \n"))
Numb5 = int(input("enter you num 5 \n"))

s ={Numb1, Numb2, Numb3, Numb4, Numb5}
print(s);



#sols 3   

s = {18, "18"};
print(s) #{18,'18'} as it is a string 


 #sols 4

s ={20 ,20.0, '20'}
print(len(s))

#output is 2 because it will take 20 and 20.0 as one length 

#sol 5
s ={}
print(type(s)) #it will be dict 


#sols 6

favLang ={}
aa = input('Enter you fvt lang shubam')
bb = input('Enter you fvt lang ankit')
cc = input('Enter you fvt lang sonali')
dd = input('Enter you fvt lang harshita')

favLang['shubam'] =  aa
favLang['ankit'] = bb
favLang['sonali'] = cc
favLang['harshita'] = dd