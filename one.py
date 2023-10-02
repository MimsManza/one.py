question = 1

def hello_name(user_name):
    print("hello_" + user_name + "!")

question = 2

def hello_name(user _name):
    print("hello_" + user _name + "!")
# call the function with a username
hello_name("John")

question = 3

def first_odds():
    odd_list = []
    for number in range(1, 1001):
        if number % 2 != 0:    
            print(number)
            odd_list .append(number)
    return odd_list

question = 4

def max_num_in_list(a_list):(input_list):
if len(input_list) == 0:
        # return none for an empty list
else:
        max_num = input_list[0] #
Initialize max_num with the first
element of the list
for num in input_list:
    if num > max_num:
        max_num = num
return max_num

def is_leap_year(year):
    # check if the year is divisible by 
 4

if year % 4 == 0:
        # if its divisible by 100, it
    must be divisible by 400 to be a 
leap year
        if year % 100 == 0:
            return True
        else:
            return False
        else:
        return True
    else: 
        return False

def is_consecutive(a_list):
    # check if the list is empty or has only one element
    if len(a_list) <= 1:

        Return 
        True

    # sort the list to ensure
consecutive numbers are in order
    sorted_nums = sorted(num)


5

def are_consecutive_numbers(list):
     # check if the list is empty or has only one element
    if not 1st or len(1st) == 1:
        return True
    
    # Sort the list in ascending order
    1st.Sort()

    #check if the difference between
adjacent elements is always 1
    for i in range(1, len(1st))
        if 1st{i} - 1st{i - 1} != 1:
            return False
        
        return True
# Example usage:
list1 = [2, 3, 4, 5, 6, 7]
list2 = [1, 2, 3, 4, 5]

print(are_consecutive_numbers(list1)) #
should return True
print(are_consecutive_numbers(list2)) #
Should return False