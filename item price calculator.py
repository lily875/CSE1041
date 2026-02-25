item_number=int(input("enter no of items "))
item_price=int(input("enter the price"))
total_price=item_number*item_price
discounted_price=(item_number*item_price)*0.10
if item_price>=1000:
    print(f"{total_price-discounted_price} is the discounted price")
else:
    print(f"{total_price}")

