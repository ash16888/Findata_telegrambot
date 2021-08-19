import requests 
def price_now(ticker):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        base_url = 'https://query1.finance.yahoo.com/v7/finance/options/'
        url = base_url + ticker.lower()
        query = {k: v for dct in requests.get(url,headers=headers).json()['optionChain']['result'] for k, v in dct.items()}['quote']
        last_price = query['regularMarketPrice'] 
        last_price = round(last_price, 2)
        day_range = query['regularMarketDayRange']
        diff = query['regularMarketChangePercent']
        diff = round(diff, 2)
        if diff >= 0:
            diff = '+' +str(diff)
        elif diff < 0:
            diff = str(diff)
        return str(last_price) + '\n' + diff + '%' + '\n' + day_range
    except LookupError:  
        return 'Я не понимаю Вас. Выберите одно из действий или введите тикер.'
