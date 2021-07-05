def currency_rates(currency):
    import requests
    import datetime
    currency = currency.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)

    for el in content.split('<Valute'):
        if currency in el:
            rate = el.split('<Value>')[1:]
            rate = rate[0].split('<')
            rate = float(rate[0].replace(',', '.'))
        if 'Date' in el:
            data = (el.split('Date="')[1]).split('"')[0]
            data = data.split('.')
            date = datetime.datetime(year=int(data[2]), month=int(data[1]), day=int(data[0]))
    return rate, date