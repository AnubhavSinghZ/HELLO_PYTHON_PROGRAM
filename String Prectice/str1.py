str1='Hello'
str2="World"
str3="""Multi line
string example"""

#2. Immutability
text="Python"
#text[0]='J' #<--- Type Error
#Correct Approach
text="J"+text[1:]


# Indexing  and  Slicing

s="DEVELOPER"
print(s[0])       # 'D'  (First character)
print(s[-1])      # 'R'  (Last character)
print(s[0:4])     # 'DEVE' (Indices 0, 1, 2, 3)
print(s[2:])      # 'VELOPER'
print(s[:4])      # 'DEVE'
print(s[::2])     # 'DVLOE' (Step by 2)
print(s[::-1])   # 'REPOLEVED' (Reverses string)