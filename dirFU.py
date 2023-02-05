import sys
import requests
import concurrent.futures
import argparse
import pyfiglet
import time
from colorama import Fore

startTime= time.time()
banner = pyfiglet.figlet_format("DirFU  ")
print(banner)

parser=argparse.ArgumentParser(
    usage= '''dirFU.py -d example.com -f /path/to/file.txt''',
    description='''DirFU a Directory Bruteforcer for beginners''',
    epilog="""Developer: @instagram.com/thecyberjerry""")
parser.add_argument('-d','--domain',required=True,help='-d example.com')
parser.add_argument('-f','--file',required=True, help='-f /path/to/file/file.txt')
args=parser.parse_args()
Target = vars(args)
url = Target.get('domain')
urls = []

with open(Target.get('file'),'r') as file:
    var = file.read().splitlines()

for item in var:
    var2 = f'https://{url}/{item}'
    urls.append(var2)
dict = {200:[]}
def main(url):
    resp = requests.get(url)
    v = f'\n{url} {Fore.YELLOW}Code: {resp.status_code}{Fore.RESET}'
    if resp.status_code == 200:
        dict[200] += [url]
    return v

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    try:
        with open('readme.md', 'r') as file:
            var = file.read()
            print(var)
        print('\t\t=========STARTED=========\n')
        for u in urls:
            futures.append(executor.submit(main, url=u))
        for future in concurrent.futures.as_completed(futures):
            print(future.result())
    except requests.ConnectionError:
        pass
    except KeyboardInterrupt as e:
        e = f'\n{Fore.WHITE}Keyboard Interrupt Detected Exiting!!\n\nResult will be saved in activeDirectory.txt File{Fore.RESET}'
        print(e)
        print("\n\t\t""=========Finished!!=========", end=(f"\n\n{Fore.YELLOW}Execution time took: " + str(time.time() - startTime) + f" seconds{Fore.RESET}"))
        var7 = '\n'.join(dict[200])
        with open('activeDirectories.txt', 'w') as active:
            active.write(var7)
        sys.exit()
var7 = '\n'.join(dict[200])
with open('activeDirectories.txt', 'w') as active:
    active.write(var7)
    print(f'\n{Fore.WHITE}Result will be saved in activeDirectory.txt File{Fore.RESET}')
    print("\n\t\t""=========Finished!!=========", end=(f"\n\n{Fore.YELLOW}Execution time took: " + str(time.time() - startTime) + f" seconds{Fore.RESET}"))
