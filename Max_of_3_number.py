# First Method: 

def max(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))
print(f"The largest of 3 Numbers you entered is: {max(a,b,c)}")

# Another Method:

def max_of_three_numbers(a, b, c):
    return max(a, b, c)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
print(f"The largest of the three numbers you entered is: {max_of_three_numbers(a, b, c)}")

