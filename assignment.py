def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """

    return(f"My name is {name} and I am {age} years old") # returing the formatted print statement

print(format_string("John", 25)) 
print(format_string("Alice", 30)) 





def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    # using if elif statement for conditional check

    if number > 10:
        return "Greater"
    elif number < 10:
        return "Lesser"
    else:
        return "Equal"

# number = int(input("Enter a number to check: ")) # asking user to provide the number (prompt)

print(conditional_check(15)) 
print(conditional_check(5)) 
print(conditional_check(10))



def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    # using for loop
    sum = 0
    for i in range(1, n + 1): # loop starts from 1 to upper limit
        sum += i
    return sum

# n = int(input("Enter the number: "))
print(loop_sum(5))
print(loop_sum(3))
print(loop_sum(1))




def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    if not numbers:
        return 0, None, None

    sum = 0  
    max_num = numbers[0]  # considering first number of numbers as max_number before comparing
    min_num = numbers[0]  # considering first number of numbers as min_number before comparing

    for num in numbers: # for loop is used to compare all elements of list
        sum += num  
        if num > max_num:   # checking condition and updating value accordingly
            max_num = num
        if num < min_num: 
            min_num = num

    return sum, max_num, min_num

# numbers = [1, 3, 5, 4, 2]
result = list_operations([1, 2, 3, 4, 5])
result1 = list_operations([10, 20, 30])
print(result)
print(result1)

        

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    result = [] # initializing the list to store the name of student above 80
    for student, score in students_dict.items(): # items helps to find keys and values of dict
        if score > 80:
            result.append(student)
    return result

# student_percentage = {'Prakash Pandey': 83, 'Ram Shrestha': 63, 'Shreya Shrestha': 81, 'Emul Ofz': 73}
students = {
        "John": 85,
        "Alice": 90,
        "Bob": 75,
        "Eve": 95
    }
result = dict_operations(students)
print(result)




def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1.intersection(set2) # intersection is used to find the common elements
    return common_elements
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
result = set_operations([1, 2, 3], [2, 3, 4])
result1 = set_operations([1, 2], [3, 4])
print(result)
print(result1)



def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    results = {
        "sum": a + b,
        "difference": a - b,
        "product": a * b,
        "quotient": a / b if b != 0 else "undefined",   
    }
    return results

a = 10
b = 5

# a = float(input("Enter the First Number: "))
# b = float(input("Enter the Second Number: "))
results = arithmetic_ops(a,b)
print (results)



def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    results = {
        "and": x and y, # high if all input is high
        "or": x or y,    # high if any one input is high
        "not_x": not x,  # opposite of x
    }
    return results

x = True
y = False
result = logical_ops(x, y)
print(result)



def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    results = {
        "and": a & b,       
        "or": a | b,        
        "xor": a ^ b,         
    }
    return results
a = 12
b = 10
# a = int(input("Enter value of a: "))
# b = int(input("Enter value of b: "))
result = bitwise_ops(a, b)
print(result)