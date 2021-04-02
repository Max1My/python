price_list = [57.8, 46.51, 97, 123.50, 59.20, 30.59, 30, 529.98, 1299.99, 5690.74, 3950.87, 3295.02, 589.90, 32.54]
if isinstance() == float:
    price = [format(flt) for flt in price_list]
    price += ' коп'
    print(price)
print(list(map(type, price_list)))