# 1. Write a program to find the second largest element in an array.
def second_largest(arr):
    arr=list(set(arr))
    if len(arr)<2:     #check if we have atleast 2 elements
        return "no second largest element"
    first=second=float('-inf')
    for num in arr:
        if num>first:
            second=first
            first=num
        elif num>second:
            second=num
    return second
user_input=input("enter numbers seperated by spaces:")
numbers=list(map(int,user_input.split()))
result=second_largest(numbers)
print("seecond largest element:",result)



# 2. Write a program to sort a list of elements in ascending order.
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

# Get input from user
input_str = input("Enter the list of numbers separated by spaces: ")
# Convert input string to a list of integers
elements = list(map(int, input_str.split()))

print("Original list:", elements)
bubble_sort(elements)
print("Sorted list (ascending):", elements)


# 3. Write a program to remove duplicates from a list.

# Get input from user
input_str = input("Enter the list of elements separated by spaces: ")
elements = input_str.split()

# Remove duplicates using set
unique_elements = list(set(elements))

print("List after removing duplicates:", unique_elements)


# 4. Write a program to find the common elements between two lists.

list1 = input("Enter elements of the first list separated by spaces: ").split()
list2 = input("Enter elements of the second list separated by spaces: ").split()

# Find common elements using set intersection
common_elements = list(set(list1) & set(list2))

print("Common elements:", common_elements)



# 5. Write a program to find the factorial of a number using recursion.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Get input from the user
num = int(input("Enter a non-negative integer: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}")



# 6. Write a program to find the LCM of two numbers.

def find_lcm(a, b):
    lcm = max(a, b)
    while True:
        if lcm % a == 0 and lcm % b == 0:
            return lcm
        lcm += 1

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = find_lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is {result}")



# 7. Write a program to implement binary search.


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Return the index where target is found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found

# Example usage:
sorted_list = list(map(int, input("Enter sorted numbers separated by spaces: ").split()))
target = int(input("Enter the target number to search: "))

result = binary_search(sorted_list, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")



# 8. Write a program to implement selection sort.


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Return the index where target is found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found

# Example usage:
sorted_list = list(map(int, input("Enter sorted numbers separated by spaces: ").split()))
target = int(input("Enter the target number to search: "))

result = binary_search(sorted_list, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")



# 9. Write a program to implement merge sort.


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle point
        left_half = arr[:mid]   # Dividing the array elements
        right_half = arr[mid:]

        merge_sort(left_half)   # Sort the first half
        merge_sort(right_half)  # Sort the second half

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy the remaining elements of left_half, if any
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy the remaining elements of right_half, if any
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Get input from user
elements = list(map(int, input("Enter numbers separated by spaces: ").split()))

merge_sort(elements)

print("Sorted list:", elements)



# 10. Write a program to implement quick sort.


def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: a list of zero or one element is sorted

    pivot = arr[len(arr) // 2]  # Choose middle element as pivot
    left = [x for x in arr if x < pivot]   # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot

    # Recursively apply quick_sort to left and right, then combine
    return quick_sort(left) + middle + quick_sort(right)

# Get input from user
elements = list(map(int, input("Enter numbers separated by spaces: ").split()))

sorted_elements = quick_sort(elements)
print("Sorted list:", sorted_elements)



# 11. Write a program to find the sum of all the prime numbers between two given numbers.

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_primes(start, end):
    total = 0
    for num in range(start, end + 1):
        if is_prime(num):
            total += num
    return total

# Get input from user
start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))

result = sum_primes(start_num, end_num)
print(f"The sum of prime numbers between {start_num} and {end_num} is {result}")



# 12. Write a program to find the sum of all the even numbers between two given numbers.


def sum_even(start, end):
    total = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            total += num
    return total

# Get input from user
start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))

result = sum_even(start_num, end_num)
print(f"The sum of even numbers between {start_num} and {end_num} is {result}")



# 13. Write a program to find the sum of all the odd numbers between two given numbers.

def sum_odd(start, end):
    total = 0
    for num in range(start, end + 1):
        if num % 2 != 0:
            total += num
    return total

# Get input from user
start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))

result = sum_odd(start_num, end_num)
print(f"The sum of odd numbers between {start_num} and {end_num} is {result}")



# 14. Write a program to find the square root of a number using the Newton-Raphson method.

def newton_raphson_sqrt(number, tolerance=1e-10, max_iterations=1000):
    if number < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    if number == 0:
        return 0

    guess = number / 2.0  # Initial guess

    for _ in range(max_iterations):
        next_guess = 0.5 * (guess + number / guess)
        if abs(next_guess - guess) < tolerance:
            return next_guess
        guess = next_guess

    return guess  # Return the last guess if tolerance not met

# Get input from user
num = float(input("Enter a non-negative number to find the square root: "))

try:
    sqrt_value = newton_raphson_sqrt(num)
    print(f"The square root of {num} is approximately {sqrt_value}")
except ValueError as e:
    print(e)



# 15. Write a program to find the power of a number using recursion.

def power(base, exponent):
    if exponent == 0:
        return 1  # Base case: any number to the power 0 is 1
    elif exponent < 0:
        return 1 / power(base, -exponent)  # Handle negative exponent
    else:
        return base * power(base, exponent - 1)

# Get input from user
base_num = float(input("Enter the base number: "))
exp_num = int(input("Enter the exponent (integer): "))

result = power(base_num, exp_num)
print(f"{base_num} raised to the power {exp_num} is {result}")




