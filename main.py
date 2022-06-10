# libraries
from colorama import Fore
import colorama
import requests
import argparse

# initialize colorama
colorama.init()

# define arguements for argparse
parser = argparse.ArgumentParser(description='Scrape valid proxies\nexample: main.py https 10000')
parser.add_argument('proxy_type', type=str, help='http, https, socks4, socks5')
parser.add_argument('proxy_timeout', type=int, help='Proxy timeout')
options = parser.parse_args()

proxy_type = options.proxy_type
proxy_timeout = options.proxy_timeout

url = requests.post(f'https://api.proxyscrape.com/v2/?request=getproxies&protocol={proxy_type}&timeout={proxy_timeout}&country=all')
try:
    print(url.text)
    f = open('proxies.txt', 'w')
    f.write(f'{Fore.GREEN}{url.text}')
except:
    pass
