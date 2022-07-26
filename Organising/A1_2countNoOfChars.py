#write a program to count the number of characters (frequency) in a string
str1=input('enter the string:')
n=len(str1)
for i in range(0,n):
    print( '\' ',str1[i],'\' ' ,':',str1.count(str1[i]),end='; ')