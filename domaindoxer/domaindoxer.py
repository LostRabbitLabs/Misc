#!/usr/bin/python3
from googlesearch import search
import os
import sys

try:
    search_term1 = sys.argv[1]
    arg1 = '"' + search_term1 + '"'
except:
    print("\nDomain Doxer ERROR!! Please provide a domain to dox using the format below and try again.\n")
    print("./domaindoxer.py example.com\n")
    sys.exit()

auth_leak_array = []
doc_leak_array = []
internal_leak_array = []
code_leak_array = []
osint_leak_array = []
pastebin_leak_array = []
malware_array = []

auth_leak_search1 = search_term1 + ' AND "haveibeenpwned|sql|user|login|username|id|uid|password|passwd|pw leak|leaked|dump|dox|doxed|pwnd|pwned|pwn3d|pii|phi" | site:http://s3.amazonaws.com ' + arg1
doc_leak_search1 = ' AND "ext:doc | ext:docx | ext:xls | ext:xlsx | ext:pdf | ext:ppt | ext:pptx | ext:txt | ext:vsd | ext:vsdx | ext:sql | ext:csv"'
internal_leak_search1 = ' AND "secret|private|draft|confidential|proprietary|attorney|privileged|internal|limited|controlled"'
code_leak_search1 = ' site:googlecode.com | site:code.google.com | site:github.com | site:devshed.com | site:stackoverflow.com | site:superuser.com | site:grokbase.com | site:snipplr.com | site:searchcode.com | site:codeplex.com | site:codepen.io | site:workingbase.com | site:codeverge.com'
osint_leak_search1 = ' AND facebook | linkedin | myspace | twitter | instagram | snapchat | vk | tiktok | alexa | crunchbase | similarweb | domainbigdata | whois '
pastebin_search1 = ' AND site:pastebin.com OR site:ghostbin.com OR site:0bin.net OR site:PasteFS.com OR site:pastiebin.com OR site:pastie.org'
malware_search1 =  'AND site:otx.alienvault.com OR site:any.run OR site:www.hybrid-analysis.com OR site:www.joesandbox.com OR site:urlscan.io'

print ("\n\n    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd:kMM  ")
print ("    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNO:. oWM  ")
print ("    MMMMMMMMMMMM |  LostRabbitLabs  | MMMMMMW0:.   lNM  ")
print ("    MMMMMMMMMMMM |                  | MMMMMXo.     :NM  ")
print ("    MMMMMMMMMMMM |  <D0main D0x3r>  | MMMWk,       :XM  ")
print ("    NK0XWMMMMMMM |      v0.1a       | MMKc.        :XM  ")
print ("    K:..,:okKNMMMMMMMMMMMMMMMMMMMMMMMMWk'          lNM  ")
print ("    Wk.     .,cd0NWMMMMMMMMMMMMMMMMMMNo.          .dWM  ")
print ("    MWk.        .'ckXMMMMMMMMMMMMMMMNl            '0MM  ")
print ("    MMWO'           'dXMMMMMMMMMMMMWd.            cNMM  ")
print ("    MMMM0;            'xNMMMMMMMMMM0'            .OMMM  ")
print ("    MMMMMXl.            ;0WMMMMMMMNl             lNMMM  ")
print ("    MMMMMMWk,            'OMMMMMMMO'            :KMMMM  ")
print ("    MMMMMMMMKl.           :KMMMMMWo            ;KMMMMM  ")
print ("    MMMMMMMMMNk,         ..;oolcc:.          .lXMMMMMM  ")
print ("    MMMMMMMMMMMXd'                  ...    .:OWMMMMMMM  ")
print ("    MMMMMMMMMMMMMXkc.   'c,         .,cc,.'kWMMMMMMMMM  ")
print ("    MMMMMMMMMMMMMMMX:  ,dc.            'c;,xNMMMMMMMMM  ")
print ("    MMMMMMMMMMMMMMNl  .'.                  .xWMMMMMMMM  ")
print ("    MMMMMMMMMMMMMM0'                        ,KMMMMMMMM  ")
print ("    MMMMMMMMMMMMMMx.                        .xMMMMMMMM  ")
print ("    MMMMMMMMMMMMMMk.              ..'''.     lNMMMMMMM  ")
print ("    MMMMMMMMMMMMMM0;;dddl;.    .ckKNWWNKo.   cNMMMMMMM  ")
print ("    MMMMMMMMMMMMMMXdkMMMMWO'   oWMMMMMMMNl   lWMMMMMMM  ")
print ("    MMMMMMMMMMMMMMWkkWMMMMX:   ;0WMMMMMMWo  .xMMMMMMMM  ")
print ("    MMMMMMMMMMMMMMM0xXMMNO:'.....lOKNNNXx'  ,KMMMMMMMM  ")
print ("    MMMMMMMMMMMMMMMXl;c:::d0xxxx3d;,'''.   .xWMMMMMMMM  ")
print ("    MMMMMMMMMMMMMMMMO'.:kNMMMdohMWN0dc,...'xWMMMMMMMMM  ")
print ("    MMMMMMMMMMMMMMMMWKKWMMMMruhrohMMMMWXKKXWMMMMMMMMMM  ")
print ("    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM  \n\n")

print ("    Now running Domain Doxer... \n\n")


try:
    search_term = auth_leak_search1
    for url1 in search(search_term, stop=40):
        auth_leak_array.append(url1)
except:
    pass
    print ("auth_leak_array error")

print ("AUTH DATA LEAKAGE for " + arg1 +":")
for result in auth_leak_array:
    result = result.split("?sa=X")[0]
    print (result + "\n")

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


try:
    search_term_doc = 'site:' + search_term1 + doc_leak_search1
    for url in search(search_term_doc, stop=40):
        doc_leak_array.append(url)
except:
    pass
    print ("doc_leak_array error")

print ("DOC DATA LEAKAGE for " + arg1 +":")
for result in doc_leak_array:
    result = result.split("?sa=X")[0]
    print (result + "\n")

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


try:
    search_term_internal = 'site:' + search_term1 + internal_leak_search1
    for url in search(search_term_internal, stop=40):
        internal_leak_array.append(url)
except:
    pass
    print ("internal_leak_array error")

print ("INTERNAL DATA LEAKAGE for " + arg1 +":")
for result in internal_leak_array:
    result = result.split("?sa=X")[0]
    print (result + "\n")

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


try:
    search_term_code = arg1 + code_leak_search1
    for url in search(search_term_code, stop=40):
        code_leak_array.append(url)
except:
    pass
    print ("code_leak_array error")

print ("CODE DATA LEAKAGE for " + arg1 +":")
for result in code_leak_array:
    result = result.split("?sa=X")[0]
    print (result + "\n")

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


try:
    search_term_osint = arg1 + osint_leak_search1
    for url in search(search_term_osint, stop=80):
        osint_leak_array.append(url)
except:
    pass
    print ("osint_leak_array error")

print ("OSINT DATA LEAKAGE for " + arg1 +":")
for result in osint_leak_array:
    result = result.split("?sa=X")[0]
    print (result + "\n")

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


try:
    search_term_pastebin = arg1 + pastebin_search1
    for url in search(search_term_pastebin, stop=20):
        pastebin_leak_array.append(url)
except:
    pass
    print ("osint_leak_array error")

print ("PASTEBIN DATA LEAKAGE for " + arg1 +":")
for result in pastebin_leak_array:
    result = result.split("?sa=X")[0]
    print (result + "\n")

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

try:
    search_term_malware = arg1 + malware_search1
    for url in search(search_term_malware, stop=60):
        malware_array.append(url)
except:
    pass
    print ("malware_array error")

print ("MALWARE DATA LEAKAGE for " + arg1 +":")
for result in malware_array:
    result = result.split("?sa=X")[0]
    print (result + "\n")

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

print ("\nDomain Doxer has completed doxing the domain. \n\n")

sys.exit()

