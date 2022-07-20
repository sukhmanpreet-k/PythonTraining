'''write a program to find the first appearance of the substring "not" and "poor" from a given string, if "not" follows the "poor", replace the whole "not"..."poor" substring with "good". return the restulting string
sample string: the lyrics is not that poor
the lyrics is poor
expected result: the lyrics is good
the lyrics is poor'''

str=input('enter the string :')
notstr='not'
poorstr='poor'
goodstr='good'
newstr=''
n=len(str)
for i in range(0,n):
    if str[i:i+3]==notstr:
        print('not found at ',i)
        for j in range(0,n):
            if str[j:j+4]==poorstr:
                print('poor found at ',j)
                if i<j:
                    newstr=str[:i]+goodstr
                else:
                    newstr=str
print(newstr)

