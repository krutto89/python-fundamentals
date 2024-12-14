def calculate_discount(price, discount_percent):
    if discount_percent >=20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    

original_price =  float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percent: "))

final_price = calculate_discount(original_price, discount_percent)
print("The final price is: ", final_price)

if final_price == original_price:
    print(f"Sorry, you are not eligible for a discount so your final price remains to be {original_price}")

else:
    print(f"final price is: ", final_price)

