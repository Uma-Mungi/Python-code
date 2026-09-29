# a = list(map(int, input().split())) 
# n=int(input()) 
# numbers = [i * n for i in a]  
# print(numbers) 

"amstrong"
# a=int(input())
# s=str(a)
# l=len(s)
# sum=0
# for each in s:
#     sum+=int(each)**1
# if sum == a:
#         print("amstrong number")
# else:
#         print("not amstrong")



"sum of n natural numbers"

# n=int(input())
# sum_n=0
# for i in range(n+1):
#     sum_n+=i
# print(sum_n)

"sum of even numbers"
# a=int(input())
# sum_n=0
# for i in range(1,a+1):
#     if(i%2==0):
#         sum_n+=i
# print(sum_n)

"n numbers divisible by k"
# n=int(input())
# k=int(input())
# count=0
# for i in range(n):
#     a=int(input())
# if(a%k==0):
#     count+=1
# print(count)

"get the first n characters from the string"
# n=input()
# k=int(input())
# print(n[k:]) 

"Lucky number"
# a=int(input())
# b=int(input())
# if(a==6 or b==6):
#     print("lucky number")
# elif (a+b==6):
#     print("lucky number")
# elif (a-b==6 or b-a==6):
#     print("lucky number")
# else:
#     print("unlucky number")



"find even and odd index in a given string"
# n=input()
# length=len(n)
# even=""
# odd=""
# for i in range(length):
#     if i%2==0:
#         even+=n[i]
        
#     else:
#         odd+=n[i]
# print("even:",even) 
# print("odd:",odd)      

"extract the digit from the given input"
"find the sum of all numbers,odd,even numbers separatelly"

# a = list(map(str,input().split()))
# s_n=0
# s_e=0
# s_o=0
# for i in a:
#     if i.isdigit():
#        s_n=int(i)
#        if int(i)%2==0:
#            s_e+=int(i)
#        else:
#            s_o+=int(i)   
# print(s_n)           
# print(s_e)
# print(s_o)

"given list is multiplied with a  specific number"
# a=list(map(int,input().split()))
# n=int(input())
# l = []
# for i in a:
#     l.append(i*n)
# print(l)
    
# n=input().split("a")
# print(n)
# s="namratha"
# for i in s:
#     print(i)

"21/06/2025"
"print n fibannoci numbers"
"the sum of its two previous numbers are equal to their third number"
"f(n)=f(n-1)+f(n-2)  the first two numbers 0&1 has to be declare at starting"
# n=int(input())
# l=[0,1]
# a=0
# b=1
# for i in range(n-2):
#     c=a+b
#     l.append(c)
#     a=b
#     b=c
# print(*l)


"u r given a string and u have to count the vowels in the given string(both upper and lower case)"
" and return the total count"
# n=input()
# c=0
# for i in n:
#     if i in "aeiouAEIOU":
#      c+=1
# print(c)

"u r given a string s ur task is to check if string is palindrome "
"if  it has same forward and backward  "
"i/p: a man a plan a canal panama"
"o/p:true"
"i/p:hello world"
"o/p:false"
# n=input().split()
# b="".join(n)
# l=b.upper()
# rev=l[::-1]
# if l==rev:
#     print("true")
# else:
#     print("false")

"ur given a string s ur task is to count the number of words in the string and return the total count"
"i/p:hello world"
"o/p:2"
"i/p:python programming is fun"
"o/p:4"
# n=input().split()
# count=0
# for each in n:
#     count+=1
# print(count)

"ur given a string s ur task is to remove duplicte characters from the string "
"while preserving the order of the first occurances and return the modified string"
"i/p:programming"
"o/p:progamin"
# n=input()
# l=""
# for i in n:
#     if i not in l:
#         l+=i
# print(l)


# def  wish():
#     print("hi how are you lahari")
# for i in range(1,100):
#     wish()


# n=input()
# def wish(n):
#     print("hello",n,"good morning")
# wish(n)

# n=int(input())
# def square(n):
#     print(n*n)
# square(n)


# n=int(input())
# def num(n):
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")
# num(n)        


# n=int(input())
# def num(n):
#     if n%2==0:
#         return"even"
#     else:
#         return"odd"
# print(num(n))   

"factorial"
# n=int(input())
# def fact(n):
#     a=1
#     for i in range(n):
#         a=a*n
#         n=n-1
#     print(a)
# fact(n)

# def cal(a,b):
#     s=a+b
#     r=a-b
#     return s,r
# x,y=cal(20,50)
# print(x)
# print(y)


def calc(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b 
    return sum,sub,mul,div
t=calc(100,50)
print("results")
for i in t:
    print(i)
