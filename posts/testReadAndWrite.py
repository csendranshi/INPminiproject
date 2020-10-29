# import random, math
#
# def OTPgen():
#     nums='0123456789'
#     otp=""
#
#     for i in range (6):
#         otp += nums[math.floor(random.random()*10)]
#
#     return otp
#
# file1 = open('textfile.txt','a+')
# file1.seek(0)
#
# addotp= OTPgen()
# with open('textfile.txt', 'r') as read_obj:
#     for line in read_obj:
#         while line == OTPgen():
#             continue
#         else:
#             file1.write(addotp+"\n")
#             print(addotp)
#             break


import random, math
import time


# Write a program to generate  a 6 digit random number
# in python such that its non-repeating, a number used
# must be written to a text file, and the next time
# u generate a random number again it should check in the text file
# if the number exists in the text file
# generate another random number otherwise else print the number generated




start = time.time()
file1 = open('textfile.txt', 'a+')
file1.seek(0)

# a=True

while 1:
    addotp = OTPgen()
    file1.seek(0)
    if addotp in file1.read():
        end = time.time()
        print("The time",end - start)
        print("exists", addotp)
        continue
    else:
        file1.write(addotp + "\n")
        # file1.write("\n")
        end = time.time()
        print(end - start)
        break
