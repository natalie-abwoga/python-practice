#This function calculates the sum of digits of a number
#The functionality used is string conversion where [int(d) for d in str(abs(num))] converts a number (even if negative) into a list of its individual digits by taking the absolute value, turning it into a string so each digit becomes a character then loops through each character, and converts them back into integers.
#The sum of the digits is then found using the inbuilt python function sum()

def sum_of_digits(num):
    digits = [int(d) for d in str(abs(num))]
    total = sum(digits)

    print("The digits are:", ", ".join(str(d) for d in digits))
    print(f"The sum of the digits in {num} is {total}")

    
#Example of the function being used 

sum_of_digits(5497)

#In the example above, the output will be The digits are: 5, 4, 9, 7 and The sum of the digits in 5497 is 25