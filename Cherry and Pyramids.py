def count_occurances_of_substring(line_no):
    s=""
    quotient = line_no//len_str
    remainder = line_no%len_str
    if(len_str>line_no):
        return 0
    else:
        for j in range(quotient):
            s+=string
            #print(string,end="")
        #print(string[:remainder])
        s+=string[:remainder]
        count = s.count(substring)
        return count


arr = []
string = str(input())
substring = str(input())
no_of_queries = int(input())

len_substring =  len(substring)
len_str = len(string)

for i in range(no_of_queries):
    nth_line = int(input()) 
    c = count_occurances_of_substring(nth_line)
    arr.append(c)
for i in range(len(arr)):
    print(arr[i])
