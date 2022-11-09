
fresh_loaf = 3.49
discount = 0.60

def message():
    amount = float(input("Please enter loaves of yesterday's bread: "))
    regular = round(fresh_loaf * amount,2)
    discounted = round(regular * discount,2)
    total = round(regular - discounted,2)
    print(f'Regular price is {regular} \nThe discount is {discounted}\nTotal is {total}')

message()
fresh_loaf = 3.49
discount = 0.60

def message():
    amount = input("Please enter loaves of yesterday's bread (q to quit): ")
    while True:
        if amount == 'q':
            break
        elif amount != '' and amount != ' ':
            amount = float(amount)
            regular = round(fresh_loaf * amount,2)
            discounted = round(regular * discount,2)
            total = round(regular - discounted,2)
            print(f'Regular price is {regular} \nThe discount is {discounted}\nTotal is {total}')
        amount = input("Please enter loaves of yesterday's bread(q to quit): ")

message()
