#! python3
# crypto.py


import requests
import bs4
import twilio

# Bitcoin
res = requests.get('https://finance.yahoo.com/quote/BTC-USD/')
res.raise_for_status
p_bitcoin = bs4.BeautifulSoup(res.text,'html.parser')
price_bitcoin = p_bitcoin.select('div span')[14].getText()

# Ethereum
res = requests.get('https://finance.yahoo.com/quote/ETHUSD=X?p=ETHUSD=X&.tsrc=fin-srch')
res.raise_for_status
ether = bs4.BeautifulSoup(res.text,'html.parser')
price_ethereum = ether.select('div span')[11].getText()

# XRP
res = requests.get('https://finance.yahoo.com/quote/XRP-USD?p=XRP-USD&.tsrc=fin-srch')
res.raise_for_status
xrp = bs4.BeautifulSoup(res.text,'html.parser')
price_xrp = xrp.select('div span')[12].getText()

# Tether
res = requests.get('https://finance.yahoo.com/quote/USDT-USD?p=USDT-USD&.tsrc=fin-srch')
res.raise_for_status
tether = bs4.BeautifulSoup(res.text,'html.parser')
price_tether = tether.select('div span')[7].getText()

# Bitcoin Cash
res = requests.get('https://finance.yahoo.com/quote/BCH-USD?p=BCH-USD&.tsrc=fin-srch')
res.raise_for_status
bitcash = bs4.BeautifulSoup(res.text,'html.parser')
price_bitcash = bitcash.select('div span')[12].getText()

# Bitcoin SV FINISH
res = requests.get('https://www.coingecko.com/en/coins/bitcoin-sv')
res.raise_for_status
bitsv = bs4.BeautifulSoup(res.text,'html.parser')
price_bitsv = bitsv.select('.no-wrap')[0].getText()

# Litecoin
res = requests.get('https://finance.yahoo.com/quote/LTCUSD=X?p=LTCUSD=X&.tsrc=fin-srch')
res.raise_for_status
litecoin = bs4.BeautifulSoup(res.text,'html.parser')
price_litecoin = litecoin.select('div span')[11].getText()

# Binance Coin
res = requests.get('https://finance.yahoo.com/quote/BNB-USD?p=BNB-USD&.tsrc=fin-srch')
res.raise_for_status
binance = bs4.BeautifulSoup(res.text,'html.parser')
price_binance = binance.select('div span')[12].getText()

# EOS
res = requests.get('https://finance.yahoo.com/quote/EOS-USD?p=EOS-USD&.tsrc=fin-srch')
res.raise_for_status
eos = bs4.BeautifulSoup(res.text,'html.parser')
price_eos = eos.select('div span')[12].getText()

# Cardano
res = requests.get('https://finance.yahoo.com/quote/ADA-USD?p=ADA-USD&.tsrc=fin-srch')
res.raise_for_status
cardano = bs4.BeautifulSoup(res.text,'html.parser')
price_cardano = cardano.select('div span')[12].getText()

# Send price as a text message
# You will need to insert your accountSID and authToken from your Twilio account,
# in addition to your provided twilio number and personal cell phone number
from twilio.rest import Client
accountSID ='################################'
authToken = '################################'
twilioCli = Client(accountSID, authToken)
twilio_number = '+###########'
cell = '+###########'

message = twilioCli.messages.create(body=f'\nPrice Snapshot \
                                    \nBitcoin: ${price_bitcoin} \
                                    \nEthereum: ${price_ethereum} \
                                    \nXRP: ${price_xrp} \
                                    \nTether: ${price_tether}\
                                    \nBitcoin Cash: ${price_bitcash}\
                                    \nBitcoin SV: ${price_bitsv}\
                                    \nLitecoin: ${price_litecoin}\
                                    \nBinance Coin: ${price_binance}\
                                    \nEOS: ${price_eos}\
                                    \nCardano: ${price_cardano}',
                                    from_=twilio_number, to=cell)
