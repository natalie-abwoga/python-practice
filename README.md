ICS 1201 Data Structures and Algorithms                                                                                             
Python Practice Questions                                                                                                          
Name: Natalie Akongo Abwoga                                                                                                        
Admission Number: 189819

This Project contains functions that carry out the following:

1. Sum of all elements in a list.
2. Check if a number is even or odd.
3. Compute factorial using a loop.
4. Reverse a string (without using [::-1] or built-in methods).
5. Factorial (Recursive)
6. Sum of Digits of a Number

Each function is in its own file with comments explaining the logic

The following are the explanations for the individual functions:                                                                   

1.Sum of all elements in a list -                                                                                           This function takes a list of numbers and adds them all together. It goes through each number one by one, keeps a running total, and gives you the final sum at the end.
![Sum of List Elements Function](https://github.com/natalie-abwoga/python-practice/blob/main/sum_list_elements.png)

2.Check if a number is even or odd - 
This function checks if a number is even or odd. It does that by dividing the number by 2 and seeing if there’s a remainder.
If there’s no remainder, it’s even and If there is a remainder, it’s odd.
![Check Even/Odd Function](https://github.com/natalie-abwoga/python-practice/blob/main/check_even_odd.png)

3.Compute factorial using a loop - This function calculates the factorial of a number using a while loop. The factorial is the product of all positive integers up to that number.The function starts with a result of 1 and multiplies it by the current number. Then it reduces the number by 1 and repeats the process until the number reaches 0. Once the loop stops, it returns the final result, which is the factorial of the number.
![Factorial Function (Loop)](https://github.com/natalie-abwoga/python-practice/blob/main/factorial_loop.png)

4.Reverse a string (without using [::-1] or built-in methods) - This function reverses a string using a for loop. It starts with an empty string and loops through each character in the input string. On each loop, it adds the current character to the front of the reversed string, gradually building the reversed version as it goes. Once the loop is done, the reversed string is returned.
![Reverse String Function (Manual)](https://github.com/natalie-abwoga/python-practice/blob/main/reverse_string_manual.png)

5.Factorial (Recursive) - 
This function calculates the factorial of a number using recursion. The factorial of a number is the product of all positive integers up to that number.The function keeps calling itself with a smaller number until it hits 0, where it stops and returns 1 (since 0! is 1 by definition). It then multiplies the number by the result of the next smaller factorial, and this continues until the factorial is fully calculated.
![Factorial Function (Recursive)](https://github.com/natalie-abwoga/python-practice/blob/main/factorial_recursive.png)


6.Sum of Digits of a Number -                                                                                             This function adds up all the digits in a number. It first converts the number to a string (so each digit can be looked at one by one), then turns each character back into an integer. After that, it uses Python’s built-in sum() function to add them all together.
![Sum of Digits Function](https://github.com/natalie-abwoga/python-practice/blob/main/sum_of_digits.png)


For my research, I referred to the websites Stack Overflow(https://stackoverflow.com/) and GeeksforGeeks(https://www.geeksforgeeks.org/python-programming-language-tutorial/).
