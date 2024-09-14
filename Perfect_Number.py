# Perfect number is a positive integer that is equal to the sum of its proper divisors excluding itself.

def is_perfect_number(n):
    if n < 1:
        return "Your entered number is not a perfect number"
    else:
        divisior = sum(i for i in range(1, n) if n%i==0)
    if(divisior == n):
        print("Your entered number is a perfect number!")
    else:
        print("Your entered number is NOT a perfect number!")


number = int(input("Enter the number: "))
is_perfect_number(number)

