import requests
import urllib3
import socket
import pyfiglet

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



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
print(bcolors['BOLD'] +"                                        Coded By Hazeem Yaseer V3.0 \n\n" + bcolors['ENDC'])


# OPEN SUBDOMAINS FILE
print(bcolors['BOLD'] + "!!! The File Should be in the Same Folder !!!\n" + bcolors['ENDC']) 
SubsFile = input(bcolors['FAIL'] + "SUBDOMAINS FILE: " + bcolors['ENDC']) 

# READ SUBDOMAINS FILE
ReadFile = open(SubsFile, "r")
Lines = ReadFile.readlines()

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
    replace('Baidu:','').
    replace('http://','').
    replace('https://','') 
    for li in Lines
]


# REMOVE DUPLICATED LINES
PerfectLines = list(set(CleanLines))
print(bcolors['BOLD'] + "\n".join(PerfectLines) + bcolors['ENDC'])

# PRINT COUNT OF REMOVED SUBS
print(bcolors['FAIL'] + "\n\n--------------------",len(CleanLines) - len(PerfectLines)," Duplicated Subdomains Removed --------------------\n\n" + bcolors['ENDC'])

# PRINT COUNT OF ALIVE SUBS
print(bcolors['OKGREEN'] + "--------------------",len(PerfectLines)," Alive Subdomains Found ---------------------------\n\n" + bcolors['ENDC'])


def Make_Requests():   
    inpt = input(bcolors['OKGREEN'] + "Do You Want to Establish Requests ??  Y/N\n" + bcolors['ENDC'])

    if inpt not in ['Y','y']: 
        quit()
        
    elif inpt == 'Y':

        # Calculate The Estamited Time To Finish
        print(bcolors['OKGREEN'] + "                     ==========================================" + bcolors['ENDC'])
        print("                     " + bcolors['OKGREEN'] + "  " + str((len(PerfectLines)*3)//60) + " Min The Estamited Time To Finish" + bcolors['ENDC'])
        print(bcolors['OKGREEN'] + "                     ==========================================\n" + bcolors['ENDC'])

        #SAVE THE DEAD SUBS
        Make_Requests.DEADSUBS = []

        #SAVE THE ALIVE SUBS
        Make_Requests.ALIVESUBS = []

        # ESTABLISH REQUESTS
        for line in PerfectLines:
            try:
                req = requests.get('https://'+line, verify=False, allow_redirects=False, timeout=3)
                print(bcolors['OKGREEN'] + str(req.url).ljust(55) + f'[{req.status_code}]' + bcolors['ENDC'])
                Make_Requests.ALIVESUBS.append(str(req.url)+"           =========>  "+str(req.status_code))
            except:
                # CATCH ALL ERRORS  
                print(bcolors['FAIL'] +  str(line).ljust(55) + "[Failed Time Out]"  + bcolors['ENDC'])
                Make_Requests.DEADSUBS.append(str(line))

        

"""        
def Check_Dead():
    inpt = input(bcolors['OKGREEN'] + "\n\nRun Dead Subdomains Check ?? Y/N\n" + bcolors['ENDC'])

    if inpt not in ['Y','y']:

        ## SAVE THE RESULT OF RESPONSE 200 ONLY
        final_result = str(Make_Requests.ALIVESUBS).replace('[','').replace(']','').replace(',','\n').replace("'","")      
        with open('result.txt', 'w+') as file:file.write(str(final_result))

        print(bcolors['OKGREEN']+ "\n----------------------- Result Saved in result.txt -----------------------\n\n" + bcolors['ENDC']) 
        quit()
        
    elif inpt == 'Y':

        # Calculate The Estamited Time To Finish
        print(bcolors['OKGREEN'] + "                     ==========================================" + bcolors['ENDC'])
        print("                     " + bcolors['OKGREEN'] + "  " + str((len(Make_Requests.DEADSUBS)*3)//60) + " Min The Estamited Time To Finish" + bcolors['ENDC'])
        print(bcolors['OKGREEN'] + "                     ==========================================" + bcolors['ENDC'])

        quit()
        #import socket
        #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #result = sock.connect_ex(('127.0.0.1',80))
        #if result == 0:
        #   print "Port is open"
        #else:
        #    print "Port is not open"
        #sock.close()
"""

Make_Requests()

## SAVE THE RESULT OF RESPONSE 200 ONLY
final_result = str(Make_Requests.ALIVESUBS).replace('[','').replace(']','').replace(',','\n').replace("'","")      
with open('result.txt', 'w+') as file:file.write(str(final_result))
print(bcolors['OKGREEN']+ "\n----------------------- Result Saved in result.txt -----------------------\n\n" + bcolors['ENDC']) 
