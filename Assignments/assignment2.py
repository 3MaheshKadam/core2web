# Q1 --divisibility test  of 4 and 5

# a = int(input("Enter a  numb"))
# if(a%4==0 and a%5==0):
#     print("NO is d ivisible by bth 4 and 5")
# else:
#     print("Num is not divisible by both 4 and 5")
'''
# Q2 -- verification of an equilateral trinagle
a = int(input("Enter an angle "))
b = int(input("Enter another angle"))
c = int(input("Enter last angle"))
if(a!=90 and b!=90 and c!=90):
    print("not an equilateral trangle")
else:
    print("its an eeuliateral triangle !!!")
'''

'''
# Q3-- check su of two numbers is even
a = int(input("Enter another number"))
b = int(input("Enter another number"))
sum = a +b
if (sum%2==0):
    print("sum of two numbers is an even no :",sum)
else:
    print("sum of two number is odd")
'''

'''
# Q4-- check if input element exists in list
b = int(input("Enter another number"))
list1 =[1,2,3]
for a in list1:
    # print(b)
    if(a ==b):
        print("elements resides in the list")
        break
        # pass
else:
    print("not in list")
        # break
'''


# # q5
# a =int(input("enter a number"))
# b=a%2
# if (b==0):
#     for i in range(a):
#         print("core2web")
# else:
#     print("try it with an even no!!!")
'''
# Q6-- odd no
a = int(input("Enter another number"))
if(a%2!=0):
    print("num is odd")

'''

'''
#Q7-- odd test of 2 inputs at a a time
a = int(input("Enter a number"))
b = int(input("Enter another number"))
if(a%2!=0 and b%2!=0 ):
    print("both are odd")
'''
'''
#Q8--  take asci character as an input and if the ASCI  no is even the print it
a =int(input("Enter a number"))
if(a%2==0):
    print(chr(a))
'''
'''
#Q9-- check if 2 input asci values are odd if odd print their sum else just print the even nos
a = int(input("Enter a number"))
b = int(input("Enter a number"))
sum = a+b
if(a%2!=0 and b%2!=0):
    print("both are odd ASCI nos")
    print("and their sum is",sum)
    print(chr(a), chr(b))
else:
    print("both are even")
    print(chr(a), chr(b))
'''

#10--  
a = int(input("Enter a number"))
b = a//8
if (b==3):
    print("remainder is 3")
