def Simple_Interest():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the interest rate: "))
    time = float(input("Enter the time period: "))

    simple_interest = (principal * rate * time) / 100

    return simple_interest

def Compound_Interest():
    principal = float(input("Enter the principal amount: "))
    rate = .05
    time = 2

    compound_interest = principal * (pow((1 + rate / 100), time)) - principal

    return compound_interest

choice = input("Enter 'S' for Simple Interest and 'C' for Compound Interest: ")
if(choice == "s"):
    print(Simple_Interest())
    
elif(choice == "c"):
    print(Compound_Interest())