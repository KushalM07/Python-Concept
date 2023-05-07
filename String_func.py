# in this we are learning about String function 

Story ="once upon a time there was a youtuber named harry who uploaded python course with notes"

print(Story[0:5]) #once

# String Functions 
print(len(Story)) #return length of String
print(Story.endswith('abcd')) # boolean value whether it ends with it or not  
print(Story.count("o")) #Count the number of character that you have entered 
print(Story.capitalize()) # Creates the first letter capital and decapitalize if first word is capital  
print(Story.find('harry')) #gives the starting index of the word that is first occurence of that word
print(Story.replace('harry','CodeWithHarry'))  #but the string should be same ie case sensitive and replace all the occurence 


#Escape character 
''' 
\n -> new line 
\t -> new tab  i.e. white space 
\ -> single quote 
\\ -> backslash 
'''
story ="harry is good .\nhe is \tvery go\\od"
print(story)

#output 
# harry is good .
# he is   very go\od