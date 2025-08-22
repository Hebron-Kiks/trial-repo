def calculate_discount(price, discount_percent):
    if discount_percent>=20:
        discount_amount= price*(discount_percent/100)
        final_price=price - discount_amount
        return final_price
    else:
        return price
    
price=float(input("Enter the the original price: " ))
discount_percent=float(input("Enter the percent discount: "))
#calculate final price
final_price=calculate_discount(price, discount_percent)
#printing values
if discount_percent>=20:
    print(f"The price after  {discount_percent}% discount is {final_price}")
else:
    print(f"No discount applied. The price will be {price}")