'''write a program to add ing at the end of a given string
if string already ends with ing then add ly 
if string is less than 3, leave it unchanged'''

str=input('enter a string:')
newstr=''
ingstr='ing'
if len(str)<3:
    newstr=str
else:
    if str[-3:]==ingstr[0:]:
        newstr=str+'ly'
    else:
        newstr=str+'ing'
print(newstr)
