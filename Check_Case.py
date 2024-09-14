def check(str):
    lowerCase = 0
    upperCase = 0
    for i in range(0, len(str)):
        if('A'<= str[i] <='Z'):
            upperCase += 1
        elif('a'<= str[i] <='z'):
            lowerCase += 1
    print(f"Number of Upper Case Character is: {upperCase}")
    print(f"Number of Lower Case Character is: {lowerCase}")

str = input("Enter the string: ")
check(str)

# Another Approach:- 

def count_case_characters(s):
    upper_case_count = sum(1 for c in s if c.isupper())
    lower_case_count = sum(1 for c in s if c.islower())
    return upper_case_count, lower_case_count


sample_string = 'The quick Brow Fox'
upper_case, lower_case = count_case_characters(sample_string)
print(f"No. of Upper case characters : {upper_case}")
print(f"No. of Lower case Characters : {lower_case}")