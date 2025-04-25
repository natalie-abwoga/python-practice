#This function reverses a string using a for loop.
#It starts with an empty string called reversed_string_manual.
#Then, it loops through each character in the input string `s`.
#On each iteration, the current character (char) is added to the front of reversed_str.
#This results in reversed_str gradually building up in reverse order as the loop goes through all characters in s.
#Finally, the reversed string is returned.

def reverse_string_manual(s):
    reversed_string_manual = ""  # Initialize an empty string to store the reversed string
    for char in s:  # Loop through each character in the input string s
        reversed_string_manual = char + reversed_string_manual  # Add the current character to the front of reversed_str
    return reversed_string_manual  # Return the reversed string


#Example of the function being used

result = reverse_string_manual("Natalie")
print("The reversed string is:", result)

#In the example above, the function will reverse the string "Natalie":
#It loops through 'n', 'a', 't', 'a', 'l', 'i', 'e' building the reversed string as:
# "e" + "i" + "l" + "a" + "t" + "a" + "n" = "eilatan"
#So the output will be: The reversed string is: eilatan
