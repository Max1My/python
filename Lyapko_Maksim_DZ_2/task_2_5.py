price_list = [57.8, 46.51, 97, 123.50, 59.20, 30.59, 30, 529.98, 1299.99, 5690.74, 3950.87, 3295.02, 589.90, 32.54]
prc_lst = []
for price in price_list:
    if type(price) == float:
        price = format(price,'.2f')
        price = str(price)
        price = price + ' коп'
        price = price.replace('.',' руб ')
        prc_lst.append(price)
    else:
        price = float(price)
        price = format(price,'.2f')
        price = str(price)
        price = price + ' коп'
        price = price.replace('.',' руб ')
        prc_lst.append(price)
print(prc_lst)