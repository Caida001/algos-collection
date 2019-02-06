Recursive Multiply: Write a recursive function to multiply two positive integers without using the
* operator. You can use addition, subtraction, and bit shifting, but you should minimize the number
of those operations.

def recursiveMul(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0
    if num2 == 1:
        return num1 

    if num2 & 1 == 0:
        return recursiveMul(num1+num1, num2 >> 1)
    else:
        return num1 + recursiveMul(num1+num1, num2 >> 1)




