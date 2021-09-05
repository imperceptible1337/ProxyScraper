from colorama import Fore
import colorama
colorama.init()
import requests

type = input(f"{Fore.LIGHTBLUE_EX}[-] What type would you like? (http, https, socks4, socks5) {Fore.YELLOW}> {Fore.RED}")

timeout = input(f"{Fore.LIGHTBLUE_EX}[-] Proxy timeout {Fore.YELLOW}> {Fore.RED}")

url = requests.post(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol={type}&timeout={timeout}&country=all")
try:
    print(url.text)
    f = open("proxies.txt", "w")
    f.write(f"{Fore.GREEN}{url.text}")
except:
    pass
