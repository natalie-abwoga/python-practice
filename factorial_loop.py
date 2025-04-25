#This function calculates the factorial of a number using a while loop.
#A factorial of a number n (written as n!) is the product of all positive integers less than or equal to n.
#In this method, a while loop is used to multiply the result by n and then reduce n until it reaches 0.
#The loop runs as long as n is greater than 0, and on each iteration, n is multiplied to the result, then reduced by 1.
#Once n reaches 0, the loop stops, and the result, which contains the factorial, is returned.

def factorial_loop(n):
    result = 1
    while n > 0:
        result = result * n  # Multiply result by current n
        n = n - 1  # Decrease n by 1
    return result

#Example of the function being used

result = factorial_loop(6)
print("The factorial of 6 is", result)

#In the example above, the loop calculates:
# 6 * 5 * 4 * 3 * 2 * 1 = 720
#So the output will be: The factorial of 6 is 720