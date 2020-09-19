import re

def count_occurances_of_substring(line_no):
    s=""
    quotient = line_no//len_str
    remainder = line_no%len_str
    if(len_str>line_no):
        return 0
        
        
    else:
        s=string*quotient
           
        s+=string[:remainder]

        count = len(re.findall(substring, s))
        return count



string = str(input())
substring = str(input())
no_of_queries = int(input())
len_str = len(string)
for i in range(no_of_queries):
    nth_line = int(input()) 
    c = count_occurances_of_substring(nth_line)
    print(c)
