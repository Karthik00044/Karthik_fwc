
# 1.Multiplication and Sum of two numbers

Num1=int(input("Enter first Number:"))
Num2=int(input("Enter second Number:"))
Mul=Num1*Num2   #MUltiplication 
Sum=Num1+Num2   #SUM
print("Multiplication of Two numbers:",Mul)#print function
print("Sum of Two numbers:",Sum)





# 2.Sum of current number and previous Number

N=int(input("Enter Number:"))
S=N+(N-1)    #sum of previous and current
print("sum of current and previous number",S)






# 3.Display numbers which are divisible by 5

for num in range(0,101):#specify range for which number are divisible
    if num%5==0:#condition for divisiblity of 5
        print("Numbers which are divisible by 5 are:",num)#print statement





# 4.printing characters at even index

print("enter the text")  #text giving statement
text=input()
print("characters at even index:")
for i in range(0,len(text),2):#even index text output statement using for loop
    print(f"Index{i}:text{i}",text[i])#print statement




# 5.removing n numbers of characters

character=input("enter the character:")
n=int(input("enter number of character to remove:"))
if n<=len(character):
         print("result:",character[n:])
else:
    print("n is too longer")







# 6.finding first and last digit of the list are same are no
list=[90,265,52,6387,90]
if list[0]==list[-1]:
    print("first and last elements are same")
else:
          print("both are different")






# 7.Counting sub strings ina string

def count_overlapping_substring(main_string, sub_string):
    count = start = 0
    while True:
        start = main_string.find(sub_string, start)
        if start == -1:
            break
        count += 1
        start += 1
    return count

# Get input from user
text = input("Enter the main string: ")
sub = input("Enter the substring: ")

print("Occurrences with overlap:", count_overlapping_substring(text, sub))






