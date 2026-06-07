import requests



def crypto_prices():
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true")
    data = response.json()

    for crypto, info in data.items():
        price = info['usd']
        change_24h = info['usd_24h_change']
        market_cap = info['usd_market_cap']
        print(f"{crypto.capitalize()}: ${price:.2f} (24h Change: {change_24h:.2f}%, Market Cap: ${market_cap:,.2f})")
        print("-"*50)       

# crypto_prices() 
