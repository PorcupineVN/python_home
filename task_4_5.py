import sys
import utils

rate, date = utils.currency_rates(sys.argv[1])
print(round(rate, 2), date.strftime("%Y-%m-%d"))
