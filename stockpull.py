import yfinance as yf

def find_stock(message: str) -> str:
    p_message=message.upper()

    if p_message[0]=='$':
        ticker=p_message[1:]

        stock=yf.Ticker(ticker)
        price=stock.info['regularMarketPrice']
        return str(price)
