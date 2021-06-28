money = float(input('Enter your desired Money\n --> $'))
number = int(money)
decimal_num = round(money - number, 2)
print(f'Total bill --> ${money}')
print(f'Dollar bill --> ${number}')
print(f'Coins --> {int(decimal_num * 100)} cents')

dollar_bill = [100, 50, 20, 10, 5, 1]
#Converting the coins list in terms of dollars, 
#Since 1 dollar  = 100 cents..
coins = [1, 0.25, 0.10, 0.05, 0.01]

#Creating the names of the coins...
coin_names = {0.25 : 'Quater(s)', 0.10 : 'Dime', 0.05 : 'Nickel', 0.01 : 'Penny'}

#Combination for the dollar bill
total = 0
for i in dollar_bill:
    if number >= i: # lets say number = 63
        occurence = number // i  # occurence = 63 // 50 == 1, floor divison gets rid of remainder
        number = number - occurence * i  # updating the number, number = 63 - (1 * 50) == 13
        total += occurence * i # updating the total for every combination
        print(f'{occurence} X {i} dollar bill, total: {total}')

#Do same for the coin aspect..
total = total
for i in coins:
    if decimal_num >= i:
        occurence = decimal_num // i
        decimal_num = decimal_num - occurence * i
        total += round(occurence * i, 2)
        print('{} X {}, total: {:.2f}'.format(int(occurence), coin_names.get(i), total))
