'''write a program to get a string from a given where all occurrences of its first char have been changed to '$' , except the first char itself
eg : sample string: 'restart' 
expected result:'resta$t' '''
str=input("Enter the string: ")
n=len(str)
modified_str=''
for i in range(1,n):
    if str[i]==str[0]:
        modified_str +='$'
    else:
        modified_str += str[i]

print("modified string:\n",str[0]+modified_str)
        