#1.Print hello world on screen

print("Hello, World!")

#3.Write a program to find the largest of three numbers.

#let a,b,c are three numbers
a,b,c=map(int,(input("Enter a,b,c:")).split())
if c>a and c>b:
    print("c is larger")
elif a>b and a>c:
    print("a is larger")
else: 
    print("b is larger")


#4.Write a program to check whether a given number is even or odd.

n=int(input("Enter number"))
if n%2==0:
    print("EVEN NUMBER");
else:
    print("ODD NUMBER");




#5.Write a program to find the sum of all the numbers in a list.

lst=[2,4,6,44,5]
n=len(lst)
Sum=sum(lst)
print("Sum of all numbers in list",Sum)


#6.Write a program to print the Fibonacci series up to a given number.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter the number of terms: "))
print("Fibonacci Series:")
for i in range(n):
    print(fibonacci(i), end=" ")



#7. Write a program to convert Celsius to Fahrenheit.

celsius = float(input("\nEnter temperature in Celsius: "))
# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")


#8. Write a program to find the factorial of a number.

n=int(input("Enter Number:"))
def fac(n):
    if n==0 or n==1:
        return 1
    else:
       return n*fac(n-1)
print("factorial of n:",fac(n))



#9. Write a program to check whether a given number is prime or not.

num = int(input("Enter a number: "))
if num <= 1:
    print(f"{num} is not a prime number.")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")



#11. Write a program to reverse a string.

s = input("Enter a string: ")

# Reverse using slicing
reversed_s = s[::-1]

print("Reversed string:", reversed_s)



#12. Write a program to find the sum of the digits of a given number.

num = int(input("Enter a number: "))
total = 0
while num > 0:
    digit = num % 10
    total += digit
    num //= 10

print("Sum of digits:", total)



#13. Write a program to check whether a given string is a palindrome or not.

s = input("Enter a string: ")
cleaned = s.lower().replace(" ", "")
# Check palindrome
if cleaned == cleaned[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


#14. Write a program to find the area of a rectangle.

length=int(input("Enter length of rectangle"));

breadth=int(input("Enter breadth of rectangle"));

Area=length*breadth
print(f"{Area} Area of Rectangle")

#15. Write a program to find the area of a circle.

Radius=int(input("Enter the radius"))
Area1=pi*Radius^2
print("area of circle",Area1)
