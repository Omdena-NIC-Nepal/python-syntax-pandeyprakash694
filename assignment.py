def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """

    return("My name is {name} and I am {age} years old")

print(format_string("Prakash Pandey", 33))


def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if number > 10:
        print("Greater")
    elif number < 10:
        print("Lesser")
    else:
        print("Equal")

number = input(int("Enter a number to check "))
result = conditional_check(number)
print(result)

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

n = input(int("Enter the number"))
print(loop_sum(n))

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
    max_num = numbers[0]  
    min_num = numbers[0] 

    for num in numbers:
        total += num  
        if num > max_num:
            max_num = num
        if num < min_num: 
            min_num = num

    return total, max_num, min_num

numbers = [1, 3, 5, 4, 2]
result = list_operations(numbers)
print(result)


        

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    student_score_above80 = []
    for student, score in students_dict.items():
        if score > 80:
            student_score_above80.append(student)
    return student_score_above80

student_percentage = {'Prakash Pandey': 83, 'Ram Shrestha': 63, 'Shreya Shrestha': 81, 'Emul Ofz': 73}
result = dict_operations(student_percentage)
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
    pass

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    pass

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    pass

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    pass