def currency_rates(currency):
    import requests
    currency = currency.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)

    for el in content.split('<Valute'):
        if currency in el:
            result = el.split('<Value>')[1:]
            result = result[0].split('<')
            result = float(result[0].replace(',', '.'))
            return result


print(currency_rates('USD'))
print(currency_rates('EUR'))
