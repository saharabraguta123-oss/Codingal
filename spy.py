import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()
print(f"{Fore.CYAN} Welcome to Sentiment Spy!{Style.RESET_ALL}")
name = input(f"{Fore.MAGENTA} Name: {Style.RESET_ALL}").strip() or "Mystery Agent"
h = []

while 1:
    x = input(f"{Fore.GREEN} >> {Style.RESET_ALL}").strip()
    if not x:
        print(f"{Fore.RED} Enter some text!{Style.RESET_ALL}")
