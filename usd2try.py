#Converting USD forecasts to TRY

def usd2try(data):
    from datetime import datetime

    import json
    import requests

    now  = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = datetime.timestamp(now)

    #An API to get live USD-TRY prices
    url = f"https://www.isbank.com.tr/_vti_bin/DV.Isbank/PriceAndRate/PriceAndRateService.svc/GetFxRates?Lang=en&fxRateType=IB&date={date}&time={time}"
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    req = requests.get(url, headers=header)
    currencies = json.loads(req.content)
    updated_usd = (currencies["Data"][0]["fxRateBuy"] + currencies["Data"][0]["fxRateSell"]) / 2
    print(f"Live USD-TRY Value: {updated_usd}\n")

    print("Forecasts\n")
    print(data * updated_usd)