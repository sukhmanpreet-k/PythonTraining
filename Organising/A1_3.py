'''write a program to get a string made of first 2 and last 2 chars from a given string.if the string is less than 2,return instead of empty string'''
str=input('Enter the string:')
n=len(str)
if n<=2:
    print(str)
else:
    print(str[0:2]+str[-2:])