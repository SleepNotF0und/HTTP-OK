import requests
import urllib3
import socket
import pyfiglet
import urllib3

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#COLORS
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

#BANNER
print("\n\n",bcolors['FAIL'] + pyfiglet.figlet_format("G E T OK", font = "alligator" ) + bcolors['ENDC']) 
print(bcolors['BOLD'] +"                                        Coded By @Hhazeem10 V2 \n\n" + bcolors['ENDC'])


#OPEN SUBDOMAINS FILE
SubsFile = input(bcolors['FAIL'] + "SUBDOMAINS FILE: " + bcolors['ENDC']) 
ResultFile = input(bcolors['OKGREEN'] + "RESULT FILE NAME: " + bcolors['ENDC'])

#READ SUBDOMAINS FILE
ReadFile = open(SubsFile, "r")
Lines = ReadFile.readlines()

#REMOVE SPACES & DNS TITLES
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
    replace('https://','').
    replace('/','')
    for li in Lines
]


#REMOVE DUPLICATED LINES
PerfectLines = list(set(CleanLines))
print(bcolors['BOLD'] + "\n".join(PerfectLines) + bcolors['ENDC'])

#PRINT COUNT OF REMOVED SUBS
print(bcolors['FAIL'] + "\n\n"+"-"*20, len(CleanLines) - len(PerfectLines)," Duplicated Subdomains Removed " + "-"*20 +"--\n\n" + bcolors['ENDC'])

#PRINT COUNT OF ALIVE SUBS
print(bcolors['OKGREEN'] + "-"*20, len(PerfectLines)," Unique Subdomains Found " +"-"*20 + "\n\n" + bcolors['ENDC'])


def Make_Requests():   
    inpt = input(bcolors['OKGREEN'] + "ESTABLISH REQUESTS ??  Y/N\n" + bcolors['ENDC'])

    if inpt not in ['Y','y']: 
        quit()
        
    elif inpt == 'Y':
        #Calculate The Estamited Time To Finish
        print(bcolors['OKGREEN'] + " "*21 + "="*40 + bcolors['ENDC'])
        print(" "*21 + bcolors['OKGREEN'] + "|  " + str((len(PerfectLines)*3)//60) + " Min The Estamited Time To Finish  |" + bcolors['ENDC'])
        print(bcolors['OKGREEN'] + " "*21 + "="*40 + "\n\n" + bcolors['ENDC'])

        #SAVE THE DEAD SUBS
        Make_Requests.DEADSUBS = []

        #SAVE THE ALIVE SUBS
        Make_Requests.ALIVESUBS = []

        #ESTABLISH REQUESTS
        for line in PerfectLines:
            try:
                req = requests.get('https://'+line, verify=False, allow_redirects=False, timeout=5)
                print(bcolors['OKGREEN'] + str(req.url).ljust(55) + f'[{req.status_code}]' + ' ' + '['+str(req.headers.get('server', 'NOT FOUND'))+']'  + bcolors['ENDC'])    
                Make_Requests.ALIVESUBS.append(str(req.url).ljust(55) + "           =========>  " + '['+str(req.status_code)+']'+' '+ '['+str(req.headers.get('server', 'NOT FOUND'))+']')
            
            except requests.exceptions.Timeout:
                print(bcolors['FAIL'] +  str(line).ljust(55) + "[Failed Time Out]"  + bcolors['ENDC'])
                Make_Requests.DEADSUBS.append(str(req.url).ljust(55) + "           =========>  " + "[Failed Time Out]")

            except requests.exceptions.RequestException:
                print(bcolors['OKGREEN'] + str(req.url).ljust(55) + f'[{req.status_code}]' + ' ' + '['+str(req.headers.get('server', 'NOT FOUND'))+']'  + bcolors['ENDC'])    
                Make_Requests.ALIVESUBS.append(str(req.url).ljust(55) + "           =========>  " + '['+str(req.status_code)+']'+' '+ '['+str(req.headers.get('server', 'NOT FOUND'))+']')
            
            except requests.exceptions.HTTPError:
                print(bcolors['FAIL'] +  str(line).ljust(55) + "[Failed Time Out]"  + bcolors['ENDC'])
                Make_Requests.DEADSUBS.append(str(req.url).ljust(55) + "           =========>  " + "[Failed Time Out]")



Make_Requests()


#SAVE THE ALIVE SUBS
final_result = str(Make_Requests.ALIVESUBS).replace(',','\n').replace("'","")
with open(ResultFile, 'w+') as file:file.write(str(final_result))
print(bcolors['OKGREEN']+ "\n\n"+"-"*21+" Result Saved in "+ResultFile + "-"*21 + bcolors['ENDC']) 

#SAVE THE DEAD SUBS
final_dead_result = str(Make_Requests.DEADSUBS).replace(',','\n').replace("'","")
with open('DEADSUBS-'+ResultFile, 'w+') as file:file.write(str(final_dead_result))
print(bcolors['FAIL']+ "\n"+"-"*21+" Result Saved in DEADSUBS-"+ResultFile + "-"*21+"\n" + bcolors['ENDC']) 