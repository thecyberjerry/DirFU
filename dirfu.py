import requests
import argparse
import sys
import time
from colorama import Fore

startTime= time.time()
def dir(z,y):
    with open('readme.md', 'r') as file:
        var = file.read()
        print(var)
    print('\n====Started====')
    var5 = {200: []}
    for item in y:
        global url
        url = f'https://{z}/{item}'
        try:
            var4 = requests.get(url, timeout=10)
            if var4.status_code == 200:
                var5[200] += [url]
                print('\n', url, Fore.BLUE + f'\n Status Code: {var4.status_code}', Fore.RESET)
            else:
                print('\n', url, Fore.YELLOW + f'\n Status Code: {var4.status_code}', Fore.RESET)

        except requests.ConnectionError:
            pass
        except KeyboardInterrupt as e:
            e = '\n KeyBoard Interrupt detected... Exiting!!'
            print(e)
            print("\n""====Finished!!====",
                  end=("\n\nExecution time took: " + str(time.time() - startTime) + " seconds"))
            var7 = '\n'.join(var5[200])
            with open('activeDirectories.txt', 'w') as active:
                active.write(var7)
            sys.exit()
    print("\n""====Finished!!====",end=("\n\nExecution time took: "+str(time.time()-startTime)+" seconds"))
    var7 = '\n'.join(var5[200])
    with open('activeDirectories.txt', 'w') as active:
        active.write(var7)

def post_dir(z,y):
    with open('readme.md', 'r') as file:
        var = file.read()
        print(var)
    print('\n====Started====')
    var5 = {200: []}
    for item in y:
        global url
        url = f'https://{z}/{item}'
        try:
            var4 = requests.post(url, timeout=10)
            if var4.status_code == 200:
                var5[200] += [url]
                print('\n', url, Fore.BLUE + f'\n Status Code: {var4.status_code}', Fore.RESET)
            else:
                print('\n', url, Fore.YELLOW + f'\n Status Code: {var4.status_code}', Fore.RESET)

        except requests.ConnectionError:
            pass
        except KeyboardInterrupt as e:
            e = '\n KeyBoard Interrupt detected... Exiting!!'
            print(e)
            print("\n""====Finished!!====",
                  end=("\n\nExecution time took: " + str(time.time() - startTime) + " seconds"))
            var7 = '\n'.join(var5[200])
            with open('activeDirectories.txt', 'w') as active:
                active.write(var7)
            sys.exit()
    print("\n""====Finished!!====",end=("\n\nExecution time took: "+str(time.time()-startTime)+" seconds"))
    var7 = '\n'.join(var5[200])
    with open('activeDirectories.txt', 'w') as active:
        active.write(var7)
parser=argparse.ArgumentParser(
    usage= '''dirfu.py -d example.com -f /path/to/file.txt''',
    description='''DirFU a Directory Bruteforcer for beginners''',
    epilog="""Developer: @instagram.com/thecyberjerry""")
parser.add_argument('-d','--domain',required=True,help='-d example.com')
parser.add_argument('-f','--file',required=True, help='-f /path/to/file/file.txt')
parser.add_argument('-p','--POST',help = '-p POST')
args=parser.parse_args()
Target = vars(args)
with open(Target.get('file'),'r') as file:
    var2 = file.read()
    x = var2.splitlines()

if Target.get('POST') == 'POST':
    post_dir(Target.get('domain'),x)

else:
    dir(Target.get('domain'),x)
