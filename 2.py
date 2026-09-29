
"day 11 &12"

"count 1's in the binary number "
"input: 0111010101  "
"output: 6 "
"input: 11101 "
"output: 4"

# n = int(input()) 
# count = 0 
# for i in str(n):
#    if i =="1":  
#      count +=1        
# print(count)

"(or)"

# s = input() 
# v = s.count("1") 
# print(v) 

"(or)"

# s = input().split("0") 
# r = "".join(s) 
# print(s) 
# print(r) 
# print(len(r))


"'''q2)reverse method have to find the qsn logic "
"input:10 "
"output: 15 "
"input:25 "
"otput:37 "
"input:50 "
"output:75"


# n=int(input("enter a no:")) 
# print(n+(n//2)) 


"Q1) Given N number of days as input, write a program to" 
"convert N number of days to years Y, weeks W and days D "
"1 year = 365days" 
"week = 7days" 
  
  
"input :- 1329" 
"output :- 3 years"
" =>3 * 365 = 1095"
"33 weeks   => 33 * 7 = 231 "
"3 days  =>   3 *1  => 3 " 
             
"input: 2561" 
"output:-"


# n = int(input())      
# y = n//365       
# w = ((n%365)//7)      
# d = (n%365)%7      
# print(y,"years") 
# print(w,"weeks") 
# print(d,"days")


"sum of the given digits input"
"23654889=> 2+3+6+5+4+8+8+9 "
"output: 45"
"input: 12345  =>1+2+3+4+5 "
"output:15"

# n = int(input()) 
# m = str(n) 
# sum = 0 
# for each in m:      
#   sum += int(each) 
# print(sum)

"(or)"

# n=int(input()) 
# l=[] 
# for i in str(n): 
#     l.append(int(i)) 
# print(l) 
# print(sum(l))

"Remove characters" 
"input 1:- Program"
"input 2 :- ogr"
"output:-pam"

# w = input() 
# r = input() 
# result ="" 
# for each in w:         
#    if each not in r: 
#      result += each 
# print(result)

"day 13"

"input format in multi line"
"find the maximum number in the given numbers" 
"input: 58" 
"input: 6547"
"input: 896"
"output:6547"


# x = int(input()) 
# y = int(input()) 
# z = int(input()) 
# print(max(x,y,z)) 


"check wheather the number"
"is perfect number or not"
"The sum of factors of the number" 
"(excluding itself) is equals to the given"  
"number then it is considered as" 
"perfect number" 
"testcase-1:-" 
"input:-6 "
"output:- Perfect number" 
"explanation :- 1,2,3 => 1+2+3 = 6"


# n= int(input()) 
# fact_sum = 0 
# for i in range(1,n):         
#   if n % i == 0: 
#      fact_sum += i 
# if fact_sum == n:     
#    print("perfect number")  
# else:      
#    print("Not perfect number")

"check a number is prime or not"
"prime number :- A number which one and" 
"itself as factors"
"input:35"
"output:not prime"

# n = int(input()) 
# factors_count = 0 
# for i in range(1,n+1):      
#     if n % i == 0: 
#       factors_count += 1 
# if factors_count == 2:      
#     print("Prime number") 
# else: 
#    print("Not a Prime number")


"return all the digits in the given string" 
"input: a1b234cd56 "
"output: 123456 "
"input: 5star3roses" 
"output :- 53"

# s = input() 
# result = "" 
# for i in s:          
#    if i.isdigit(): 
#       result += i 
# print(result)


"find the elements that are even number of times repeated"
"input:-1  1 1 2 2  2 2 2  2 3 3 4 4  4 4 4"
"output:-2 3"

# n = list(map(int, input ().split())) 
# l = [] 
# for each in n:          
#     cnt = n.count(each) 
#     if cnt % 2 == 0: 
#       if each not in l: 
#         l.append(each) 
# print(*l) 

"or"

# n = list(map(int, input ().split())) 
# s = list(set(n)) 
# l = [] 
# for each in s:               
#    cnt = n.count(each) 
#    if cnt % 2 == 0: 
#     if each not in l: 
#       l.append(each) 
# print(*l)

"first unique element in the list"
"input : 4 7 9 7 2 5 8 4 7 2 8 4" 
"output: 9"

# n =list(map(int,input().split())) 
# for each in n:       
#   cnt = n.count(each)  
#   if cnt ==1: 
#       print(each)
#       break

'''first non-repeated char and 
f
 irst most repeated char in a string ''' 
'''input:"abcdededdeegg 
output:a d 
explanation :- "a" because a was not repeated 
and it is the first non-repeated char  
d because "d" was repeated most no of times '''

# s = input() 
# l = [] 
# max = 1 
# for i in s:          
#   if s.count(i) == 1: 
#    l.append(i) 
#    break 
# for j in s:     
#    cnt = s.count(j)              
#    if cnt  > max : 
#      max = cnt 
#      val = j 
# l.append(val) 
# print(*l)

"if n is odd or n is even and in the range of 6 to 20 then print weird"
"if n is even and in the range of 2 to 5 or greater  than 20 print not6 weird"
# n=int(input())
# if(((n%2==0) or (n%2!=0)) and n in range(6,20)):
#         print("weird") 
# elif(((n%2==0) and n in range(2,5))):
#         print("not weird")
# else:
#         print("not weird")   
 
 
 
 
"update a value"
# s={10,20,30}
# l=[40,50,60,10]
# s.update(l,range(5))
# print(s)
"removes random element"
# s={20,30,50,40,50}
# print(s)
# print(s.pop())
# print(s)
"update using range"

# s={10,60,80,70}
# s.update(range(1,10,2),range(0,10,2))
# print(s)

