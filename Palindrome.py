str_num = input("Enter a number: ")

def check_palindrome(n):
    if(n == n[::-1]):
        return "The given number is palindrome!"
    else:
        return "The given number isn't palindrome!"

print(check_palindrome(str_num))