'''write a program to find the first appearance of the substring "not" and "poor" from a given string, if "not" follows the "poor", replace the whole "not"..."poor" substring with "good". return the restulting string
sample string: the lyrics is not that poor
the lyrics is poor
expected result: the lyrics is good
the lyrics is poor'''

str=input('enter the string :')
goodstr='good'
newstr=''
nt=str.find('not')
poor=str.find('poor')
if nt<poor and nt!=-1:
    newstr=str[0:nt]+goodstr
else:
    newstr=str
print(newstr)