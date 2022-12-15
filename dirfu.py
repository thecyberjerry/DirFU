import requests
from colorama import Fore

def dir(z,y):
    for item in y:
        global url
        url = f'https://{z}/{item}'
        try:
            var4 = requests.get(url,timeout=10)
            print('\n',url,Fore.YELLOW + f'\n Status Code: {var4.status_code}',Fore.RESET)
            requests.get(url)
        except requests.ConnectionError:
            pass
    return "\nFinished!! "

with open('readme.md','r') as file2:
    var5 = file2.read()
    print(Fore.GREEN,var5,Fore.RESET,'\n')
var = input(Fore.BLUE+ "Enter Your Domain: "+Fore.RESET)
with open('list.txt','r') as file:
    var2  = file.read()
    x = var2.splitlines()
print(dir(var,x))

