from urllib.request import urlopen
import hashlib
from termcolor import colored

hash = input("[+] Enter sha256 Hash value: ")

try:
 password_list = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read(), 'utf-8')
 for password in password_list.split('\n'):
  magic = hashlib.sha256(bytes(password,'utf-8')).hexdigest()
  if magic == hash:
   print(colored("[+] The password is: "+str(password),'green'))
   break
  elif magic != hash:
   continue
  else:
   print(colored("Password not found, try a different list!",'red'))
except Exception as exc:
 print('Something wrong: %s' % (exc))
