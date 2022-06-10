import requests
from datetime import datetime
from decimal import Decimal

def currency_rates(valute_name = '', URL="http://www.cbr.ru/scripts/XML_daily.asp"):
    valute_name = valute_name.upper()

    response = requests.get(URL)
    if response.ok:
        records = response.text.split(valute_name)
        if len(records) == 1:
            return None
        value = records[1].split("</Value>")[0].split("<Value>")[1]
        value = Decimal(value.replace(",", "."))
        date_server = response.headers["Date"]
        date_server = datetime.strptime(date_server, "%a, %d %b %Y %H:%M:%S GMT").date()
        return value, str(date_server)
    else:
        return None

print(currency_rates('EUR'))
print(currency_rates('UsD'))
print(currency_rates('Sup'))

if __name__ == '__main__':
    currency_rates('EUR')
