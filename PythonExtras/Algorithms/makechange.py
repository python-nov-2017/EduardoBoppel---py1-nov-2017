def change(cents):
    dollars = cents / 100
    remainder = cents % 100

    quarters = remainder / 25
    remainder = remainder % 25    

    dimes = remainder / 10
    remainder = remainder % 10

    nickels = remainder / 5
    pennys = remainder % 5

    coins = {
        "dollars": dollars,
        "quarters": quarters,
        "dime": dimes,
        "nickel": nickels,
        "penny": pennys
    }

    return coins



input = 105
print (change(input))