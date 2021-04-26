import math


def local(change):  # Give greedy change
    change = change * 100
    # while change >= 500:
    #     print(change // 500, "five dollars")
    #     change = change % 500
    #     continue
    # while change >= 100:
    #     print(change // 100, "one dollar")
    #     change = change % 100
    #     continue
    while change >= 25:
        print(change // 25, "quarter")
        change = change % 25
        break
    while change >= 10:
        print(change // 10, "dimes")
        change = change % 10
        break
    while change >= 5:
        print(change // 5, "quarter")
        change = change % 5
        break
    else:
        print("0 cents")


def payment_due(prices):
    x = prices // 1
    b = prices % 1
    y = (b * 100)
    if x <= 0:
        print(f"Payment_due: {math.trunc(y)} cents")
    else:
        print(f"Payment_due: {math.trunc(x)} dollars and {math.trunc(y)} cents")


def price_for_purchase(prices):
    sum_of_price = 0
    nickel = 25
    dimes = 25
    quarter = 25
    ones = 0
    fives = 0
    #global quarter, dimes, nickel, ones, fives
    while sum_of_price < prices:
        price_const = prices
        cash = input("Indicate your deposit: ")
        if cash == "c":
            print("take the change below.")
            change = sum_of_price-0
            local(change)
            break
        if cash == "q":
            sum_of_price = sum_of_price + 0.25
            price_const = price_const - sum_of_price
            quarter = quarter + 1
            if sum_of_price < prices:
                payment_due(price_const)
            else:
                change = sum_of_price - prices
                local(change)

        elif cash == "d":
            sum_of_price = sum_of_price + 0.1
            price_const = price_const - sum_of_price
            dimes = dimes + 1
            if sum_of_price < prices:
                payment_due(price_const)
            else:
                change = sum_of_price - prices
                local(change)
        elif cash == "n":
            sum_of_price = sum_of_price + 0.05
            price_const = price_const - sum_of_price
            nickel = nickel + 1
            if sum_of_price < prices:
                payment_due(price_const)
            else:
                change = sum_of_price - prices
                local(change)

        elif cash == "o":
            sum_of_price = sum_of_price + 1
            price_const = price_const - sum_of_price
            ones = ones + 1
            if sum_of_price < prices:
                payment_due(price_const)
            else:
                change = sum_of_price - prices
                local(change)
        elif cash == "f":
            sum_of_price = sum_of_price + 5
            price_const = price_const - sum_of_price
            fives = fives + 1
            if sum_of_price < prices:
                payment_due(price_const)
            else:
                change = sum_of_price - prices
                local(change)
        else:
            print("invalid input")


# main program
nickel = 25
dimes = 25
quarter = 25
ones = 0
fives = 0
store = [nickel, dimes, quarter, ones, fives]
store1 = store
print(f''' Welcome to the vending machine change maker initialized.
        stock
        contains:
            {store[0]} nickels
            {store[1]} dimes
            {store[2]} quarters
            {store[3]} 0ne dollars
            {store[4]} five dollars
           ''')
try:
    while True:
        price = input("Enter price the purchase price(xx.xx) or 'q' to quit: ")
        if price == "q":
            print("you quit")
            break
        prices = float(price)
        if (prices < 0) or ((prices * 100.0) % 5 != 0):
            print("Illegal price: must be a non-negative multiple of 5 cents")
            continue
        else:
            print('''
                    Menu for deposit:
                    'n' -deposit a nickel
                    'd' -deposit a dime
                    'q' -deposit a quarter
                    'o' -deposit a one dollar bill
                    'f' -deposit a five dollar bill
                    'c' -cancel the purchase
                    ''')
            payment_due(prices)
        price_for_purchase(prices)
        break
except ValueError:
    print("invalid input")
