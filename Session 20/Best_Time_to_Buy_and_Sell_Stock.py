prices=list(map(int,input("\nEnter stock prices separated by spaces = ").split()))
min_price=float('inf')
max_profit=0
for price in prices:
    if price<min_price:
        min_price=price
    elif price-min_price>max_profit:
        max_profit=price-min_price
print(max_profit)

# Output
# Enter stock prices separated by spaces = 7 1 5 3 6 4        
# 5