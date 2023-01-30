from collections import Counter

number_of_shoes = int(input())
all_shoe_sizes = list(map(int, (input().split())))
number_of_costumers = int(input())

sales_made = list()
stock = Counter(all_shoe_sizes)

for i in range(number_of_costumers):
    size, price = map(int, input().split())
    
    if stock[size] > 0:
        stock[size] -= 1
        sales_made.append(price)

print(sum(sales_made))
