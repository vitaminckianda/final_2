import math


def vat(price, vat_ratio):
    sales_tax = price * (vat_ratio / 100)
    return round(sales_tax, 2)


def tip(price, vat_ratio, time_of_the_day, after_tax):
    if (time_of_the_day >= 5 and time_of_the_day < 16) or (time_of_the_day <= 4 or time_of_the_day >= 17):
        tip_percentage = 0.15
    else:
        tip_percentage = 0.20

    if after_tax:
        base_price = price - vat(price, vat_ratio)
    else:
        base_price = price

    tip_amount = base_price * tip_percentage
    return round(tip_amount, 2)


def total(price, vat_ratio, time_of_the_day, after_tax):
    sales_tax = vat(price, vat_ratio)
    tip_amount = tip(price, vat_ratio, time_of_the_day, after_tax)

    if after_tax:
        total_amount = price + tip_amount
    else:
        total_amount = price + sales_tax + tip_amount

    return round(total_amount, 2)


while True:
    print("Choose a function to execute:")
    print("1. Calculate VAT")
    print("2. Calculate Tip")
    print("3. Calculate Total")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        price = float(input("Enter the price: "))
        vat_ratio = float(input("Enter the VAT ratio: "))
        result = vat(price, vat_ratio)
        print(f"VAT Amount: ${result}")
    elif choice == '2':
        price = float(input("Enter the price: "))
        vat_ratio = float(input("Enter the VAT ratio: "))
        time_of_the_day = int(input("Enter the time of the day (0-23): "))
        after_tax = input("Include sales tax in tip calculation? (True/False): ").lower() == 'true'
        result = tip(price, vat_ratio, time_of_the_day, after_tax)
        print(f"Tip Amount: ${result}")
    elif choice == '3':
        price = float(input("Enter the price: "))
        vat_ratio = float(input("Enter the VAT ratio: "))
        time_of_the_day = int(input("Enter the time of the day (0-23): "))
        after_tax = input("Include sales tax in total calculation? (True/False): ").lower() == 'true'
        result = total(price, vat_ratio, time_of_the_day, after_tax)
        print(f"Total Amount: ${result}")
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
