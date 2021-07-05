import utils

rate, date = utils.currency_rates('USD')
print(round(rate, 2), date.strftime("%Y-%m-%d"))

rate, date = utils.currency_rates('EUR')
print(round(rate, 2), date.strftime("%Y-%m-%d"))
