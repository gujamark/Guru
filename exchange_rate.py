from bs4 import BeautifulSoup
import requests

def get_exchanges():
    r = requests.get(
        "https://bankofgeorgia.ge/ge/services/treasury-operations/exchange-rates")
    soup = BeautifulSoup(r.text, "html.parser")

    exchanges = {

    }

    table = soup.find("table", attrs={"id": "AllDataTable"})
    rows = table.find("tbody").find_all("tr")

    for row in rows:
        currency = row.text.split()
        currency_info = {
            "ვალუტის დასახელება": " ".join(currency[2:len(currency) - 2]),
            "გაყიდვა": currency[len(currency) - 2],
            "ყიდვა": currency[len(currency) - 1]
        }

        exchanges[currency[1]] = currency_info

    return exchanges