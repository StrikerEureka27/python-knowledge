sellerName = input('Type your name: ')
salesAmount = input('Type your total sales: ')

salesAmount = float(salesAmount)
totalAmount = round((salesAmount * 13) / 100, 2)

print(f'\nHey! {sellerName}\n, your total comissions are ${totalAmount}')
