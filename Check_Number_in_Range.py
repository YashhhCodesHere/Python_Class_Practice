def numInRange(number, end, start):
    if(start <= number <= end):
        return "Number lies in your range!"
    else:
        return "Number does NOT lie in your range!"

number = int(input("Enter the number to check: "))
end = int(input("Enter the upper limit: "))
start = int(input("Enter the lower limit: "))
print(numInRange(number, end, start))
