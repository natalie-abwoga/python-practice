#This function returns the sum of all elements in a list
#The functionality used in this is a for loop to go through each number in the list one at a time. The loop helps it keep adding each number to the total until all numbers have been processed.

def sum_list_elements(numbers):
    total = 0
    for each_num in numbers:
        total = total + each_num
    return total 

#Example of the function being used 

print(sum_list_elements([5,8,6,3]))

#In the example, it adds 5 + 8 + 6 + 3, which gives 22.

