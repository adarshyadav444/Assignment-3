# Problem Statement: Write a Python program that:
# 1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
# 2.   Returns the calculated factorial.
# 3.   Calls the function with a sample number and prints the output.


#Using While Loop
# def factorial(n):
#     fact = 1
#     while n > 0:
#         fact = fact * n
#         n -= 1
#     return fact

# n = int(input("Please Enter Your Number: "))
# print(f"Factorial of {n} is: {factorial(n)}")

#Using For Loop
# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact * i
#     return fact
# n = int(input("Please Enter Your Number: "))
# print(f"Factorial of {n} is: {factorial(n)}")

#Using Recursion 
def factorial(n):
    if n <= 1:
        return 1
    else:
        return factorial(n-1) * n

n = int(input("Please Enter Your Number: "))
print(f"Factorial of {n} is: {factorial(n)}")





