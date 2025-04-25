#This function calculates the factorial of a number using recursion.
#A factorial of a number n (written as n!) is the product of all positive integers less than or equal to n.
#The function uses a recursive approach, meaning it calls itself with a smaller value each time.
#The base case is when n is 0. By definition, 0! is 1, so it returns 1.
#Otherwise, it multiplies n by the factorial of (n - 1) and keeps going until it reaches 0.

def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n-1)

#Example of the function being used 

result = factorial_recursive(8)
print("The factorial of 8 is", result)

#In the example above, the function will calculate:
#8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 40320
#So the output will be: The factorial of 8 is 40320