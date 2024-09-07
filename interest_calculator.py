def interest():

    try:
        amount = int(input("Enter Principle Amount: "))
        years = int(input("Enter for How many Years: "))
        int_rate = float(input("Enter interest rate: "))

        i = (amount * years * int_rate ) / 100
        return f"--> Your total interest amount is {str(i)} Rs. \n--> Your EMI amount is {str((i+amount)/(12 * years))} Rs."

    except Exception as e:
        print(e)
        print("Please enter numeric value only.")


a = interest()
print(a)
