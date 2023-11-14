# # # # # # # for i in range(11):
# # # # # # #     print(i)

# # # # # # for i in range(1 ,101):
# # # # # #     print(i)

# # # # # # for i in range(100,111):
# # # # # #     print(i)

# # # # # for i in range(1,101):
# # # # #     if(i%2==0):
# # # # #         print(i)

# # # # for i in range(1,51):
# # # #     if(i%2!=0):
# # # #         print(i)

# # # for i in range(100,0,-1):
# # #     print(i)

# # for i in range(12,121,12):
# #     print(i)

# for i in range(120 ,11,-12):
#     print(i)

# sum =0
# for i in range(1,11):
#     sum+=i
#     print(sum)


# prod =1
# for i in range(1,11):
#     prod*=i
#     print(prod)

# /////////////////////////////////////////// Assignent no 4 ///////////////////////////////

# for i in range(100 ,110):
#     print(i)

# for i in range(10 , 20):
#     if(i%2==0):
#         print(i)

# sum =0
# for i in range(1,10):
#     sum+=i
#     print(sum)

'''

start = int(input("Enter input number"))
end = int(input("Enter input number"))

for i in range(start , end):
    if(start>=65 and end<=89):
        # print("the charct of ASCII value ",start ,"is",chr(start))
        print("the charct of ASCII value ",i ,"is",chr(i))
        # print("the charct of ASCII value ",end ,"is",chr(end))
else:
    print("enter correct numbers")
'''

# for i in range(1 , 100):
#     if(i%7==0 and i%3!=0):
#         print(i)
'''
start = input("Enter starting ASCII value: ")
end = input("Enter ending ASCII value: ")

# Convert input strings to integers
start = ord(start)
end = ord(end)

if 65 <= start <= 90 and 65 <= end <= 90:
    for i in range(start, end):
        print("The character of ASCII value", i, "is", chr(i))
else:
    print("Enter correct ASCII values in the range A-Z.")
'''

# start = -7
# end = 8

# print("Positive numbers in the range from", start, "to", end, "are:")
# for i in range(start, end + 1):
#     if i > 0:
#         print(i)

start = -7
end = 8

print("negative numbers in the range from", start, "to", end, "are:")
for i in range(start, end + 1):
    if i < 0:
        print(i)
