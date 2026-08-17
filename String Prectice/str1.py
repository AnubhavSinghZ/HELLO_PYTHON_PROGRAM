str1='Hello'
str2="World"
str3="""Multi line
string example"""

#2. Immutability
text="Python"
#text[0]='J' #<--- Type Error
#Correct Approach
text="J"+text[1:]