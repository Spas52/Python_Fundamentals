product = input()
count_of_product = int(input())


def calculation_the_price_of_product(product_name,number_of_products):
    product_price = 0
    bill = None
    if product_name == "coffee":
        product_price = 1.50
        bill = product_price * number_of_products
    elif product_name == "water":
        product_price = 1.00
        bill = product_price * number_of_products
    elif product_name == "coke":
        product_price = 1.40
        bill = product_price * number_of_products
    elif product_name == "snacks":
        product_price = 2.00
        bill = product_price * number_of_products
    return bill


print(f"{calculation_the_price_of_product(product, count_of_product):.2f}")