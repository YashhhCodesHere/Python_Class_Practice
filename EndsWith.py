def check(str):
    if("you" in str.lower()):
        print("The string ends with the pattern!")
    else:
        print("It doesn't ends with that!")

check(input("Enter your pattern: "))

def check_ends_with(str, pattern):
    if (str.lower().endswith(pattern.lower())):
        print("The string ends with the pattern!")
    else:
        print("It doesn't end with that!")

check_ends_with(input("Enter your string: "), input("Enter your pattern: "))

