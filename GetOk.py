import requests
import urllib3
import socket
import pyfiglet

## COLORS
bcolors = {
    'HEADER' : '\033[95m',
    'OKBLUE' : '\033[94m',
    'OKCYAN' : '\033[96m',
    'OKGREEN' : '\033[92m',
    'WARNING' : '\033[93m',
    'FAIL' : '\033[91m',
    'ENDC' : '\033[0m',
    'BOLD' : '\033[1m',
    'UNDERLINE' : '\033[4m'
}

## BANNER
print("\n\n",bcolors['FAIL'] + pyfiglet.figlet_format("G E T OK", font = "alligator" ) + bcolors['ENDC']) 
print(bcolors['BOLD'] +"                                        Coded By Hazeem Yaseer V2.0 \n\n" + bcolors['ENDC'])


# OPEN SUBDOMAINS FILE
SubsFile = open("E:/Tools/GETOk/subs.txt", "r")
Lines = SubsFile.readlines()

# REMOVE SPACES & DNS TITLES
CleanLines = [
    li.replace(' ','').
    replace('\n','').
    replace('SSL Certificates:','').
    replace('SSLCertificates:','').
    replace('DNSdumpster:','').
    replace('Netcraft:',''). 
    replace('Bing:','').
    replace('Virustotal: ','').
    replace('Ask:','').
    replace('ThreatCrowd:','').
    replace('PassiveDNS:','').
    replace('Google:','').
    replace('Yahoo:','').
    replace('Baidu:','')  
    for li in Lines
]


# REMOVE DUPLICATED LINES
PerfectLines = list(set(CleanLines))
print(bcolors['BOLD'] + "\n".join(PerfectLines) + bcolors['ENDC'])

# PRINT COUNT OF REMOVED LINES
print(bcolors['FAIL'] + "\n\n--------------------",len(CleanLines) - len(PerfectLines)," Duplicated Lines Removed --------------------\n\n" + bcolors['ENDC'])


def Make_Requests():
    
    inpt = input(bcolors['OKGREEN'] + "Do You Want to Establish Requests ??  Y/N\n" + bcolors['ENDC'])

    if inpt not in ['Y','y']: 
        quit()

    elif inpt == 'Y':    
        # HANDLE SSL ERROR
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        # ESTABLISH REQUESTS
        Make_Requests.finaly = []
        for line in PerfectLines:
            try:
                req = requests.get('https://'+line, verify=False, allow_redirects=False, timeout=3)
                print(bcolors['OKGREEN'] + str(req.url).ljust(55) + f'[{req.status_code}]' + bcolors['ENDC'])
                Make_Requests.finaly.append(str(req.url)+"=========>"+str(req.status_code))
            except:    # CATCH ALL ERRORS 
                print(bcolors['FAIL'] +  str(line).ljust(55) + "[Failed Time Out]"  + bcolors['ENDC'])

Make_Requests()

## SAVE THE RESULT OF RESPONSE 200 ONLY
final_result = str(Make_Requests.finaly).replace('[','').replace(']','').replace(',','\n')     
with open('result.txt', 'w+') as file:file.write(str(final_result))