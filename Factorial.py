def factorial(n):
    fact = 1
    if(n<0):
        return "Enter a Non-Negative Integer!"
    elif(n == 0 or n == 1):
        return 1
    else:
        for i in range(2, n+1):
            fact *= i
        return fact


n = int(input("Enter a number: "))
print(factorial(n))

# Another method using recursion:-

def factorial_recursive(n):
    if n < 0:
        return "Enter a Non-Negative Integer!"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example usage
n = int(input("Enter a number for recursive factorial: "))
print(factorial_recursive(n))