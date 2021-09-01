

vcount = 0
vsum = 0
full_name = str(input("Enter Full Name: "))
min_price =float(input("Enter Min Price: "))
price_list = [69.0, 71.0, 84.5, 91.0, 67.4, 81.2, 84.6, 58.8, 79.3, 101.2]
for price in price_list:
    vsum = price + vsum
    if price > min_price:
        vcount = vcount +1
    
print("Hello",full_name,"the minimum price is ",min_price)
print("There are ",vcount,"prices greater than the minimum price")
print( "The total price is ",vsum)


