import requests
import xml.etree.ElementTree as et
from decimal import Decimal

# Конвертация
def currency_rates(valute):
    select_currency = {k: v for k, v in get_currency.items() if k == valute}
    if valute not in select_currency:
        print('None')
    else:
        for value in select_currency:
            select_currency[value] = select_currency[value].replace(',', '.')
            print(select_currency)
        valute1 = float(select_currency[value])
        valute1 = (rubble / valute1)
        valute1 = Decimal(valute1)
        print(valute1.quantize(Decimal("1.00")))

# Адрес api метода для запроса get
url = 'http://www.cbr.ru/scripts/XML_daily.asp'
# Отправляем get request (запрос GET)
response = requests.get(url)
tree = et.ElementTree(et.fromstring(response.text))
root = tree.getroot()
# Создаем словарь из полученного
get_currency = {}
for valute in root.findall('Valute'):
    charcode = valute.find('CharCode').text
    valute_count = valute.find('Value').text
    get_currency.update({charcode: valute_count})
# Выбор валюты
select_row = {}
rubble = int(input("Введите сумму рублей которые хотите сконвертировать: "))
select_valute = input('Введите валюту: ')
select_valute = select_valute.upper()
currency_rates(select_valute)