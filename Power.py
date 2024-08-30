num = int(input("Enter a number: "))
power = int(input("Enter the power you want: "))

def custom_power(base, exponent):
    return base ** exponent 

print(f"Answer is: {custom_power(num, power)}")

# This calculates the power of a string which will gonna throws a error.

def custom_power_string(base, exponent):
    return base ** exponent 
base = "Heyyyy"
exponent = "hello"
print(custom_power_string(base, exponent)) 