#This function checks whether a number is even or odd
#The functionality used is the modulus operator which is used to find the remainder after dividing one number by another. For even numbers, when they are divided by 2, the remainder is always 0. If the remainder is 1 then it is an odd number.

def check_even_odd(num):
    if num % 2 ==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

#Example of the function being used

check_even_odd(24)
check_even_odd(13)

#In the example above for the first instance the function will return 24 is even since 24 divide by 2 is 12 without any remainder. For the second instance it will return 13 is odd is 13 divided by 2 is 6 remainder 1