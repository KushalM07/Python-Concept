'''
-> WAP to display a  user entered name follwed by  Good AfterNoon using input() function
-> WAP to fill in a letter template given below with name and date 
    letter = " dear <|Name|> you are selected <|Date|>"
    
-> WAP to detect double spaces in a string
-> Replace the double spaces from problem 3  with single spaces
'''
#sol 1 

name = input('Enter your Name for greeting ')
print("Goood AfterNoon\n" + name)


#sol 2  

letter = ''' 
Dear <|Name|>,
you are selected  
Date : <|Date|>
'''
Name = input("Enter your name \n")
Date = input("Enter Date \n")
#we do letter = letter because it will not get replaced but simply create a new file
letter = letter.replace('<|Name|>', Name)  
letter = letter.replace('<|Date|>', Date)
print(letter)


#sol 3 

doubleSpace  = ''' this is a double Space File now  find where the  double space is '''

st  = doubleSpace.find('  ')
print('index of double space ' ,    st)

#sol 4
doubleSpace =  doubleSpace.replace('  ',' ');
print(doubleSpace)
 