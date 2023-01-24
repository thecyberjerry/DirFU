import requests
import threading
import argparse
import sys
from colorama import Fore
import pyfiglet
banner = pyfiglet.figlet_format("DirFU")
print(banner)

def dir(z,y):
    with open('readme.md', 'r') as file:
        var = file.read()
        print(var)
    print('====Started====')
    for item in y:
        global url
        url = f'https://{z}/{item}'
        try:
            var4 = requests.get(url,timeout=10)
            print('\n',url,Fore.YELLOW + f'\n Status Code: {var4.status_code}',Fore.RESET)
            requests.get(url)
        except requests.ConnectionError:
            pass
        except KeyboardInterrupt as e:
            e = '\n KeyBoard Interrupt detected... Exiting!!'
            print(e)
            sys.exit()

    return "\nFinished!! "

parser=argparse.ArgumentParser(
    usage= '''dirfu.py -d example.com -f /path/to/file.txt''',
    description='''DirFU a Directory Bruteforcer for beginners''',
    epilog="""Developer: @instagram.com/thecyberjerry""")
parser.add_argument('-d','--domain',required=True,help='-d example.com')
parser.add_argument('-f','--file',required=True, help='-f /path/to/file/file.txt')
args=parser.parse_args()
Target = vars(args)
with open(Target.get('file'),'r') as file:
    var2 = file.read()
    x = var2.splitlines()
thread = threading.Thread(target=dir(Target.get('domain'),x))
thread.start()

