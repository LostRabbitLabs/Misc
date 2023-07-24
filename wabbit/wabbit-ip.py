#!/usr/bin/python
import requests
import sys
import socket
from ipwhois import IPWhois
from bs4 import BeautifulSoup
import json
from pysafebrowsing import SafeBrowsing

gsb_apikey = ""

user_agent = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 Chrome/36.0.1985.125 Safari/537.36'}
content_type = {'Content-Type': 'application/json'}

print("\n\n                                                           ")
print("      .'...                                 ..'..          ")
print("     .dKK0Okdc,.                      .':oxO0KKO;          ")
print("      :OXXXXNNXKkl,.               .cd0XNNNXXXKd.          ")
print("       ,kXNNNNNNNNXOl.          .;xXNNNNNNNNN0l.           ")
print("        .cONWWWWWNNNW0c.       ,xNWNNWWWWWNKd'             ")
print("          .;oOXWWWWWWWNx.    .cKWWWWWWWN0xc.               ")
print("             ..,coxKNWWW0doookNWWWNOdl;'.                  ")
print("                 .:kNMMMWWMMMMMMMWXd,.                     ")
print("               .oKNWMMMMMMMMMMMMMMWWNO:.                   ")
print("              :0WWWMMMMMMMMMMMMMMMMWWWNk'                  ")
print("             cXWN0ooOWMMMMMMMMMMMXxlxXWNO,                 ")
print("            'OWWO;co,dWMMMMMMMMMXc;o;cKWNd.                ")
print("            ,0WNo.lx.;XMMMMMMMMMO.;k;.kWNx.                ")
print("            .dNNx....lNMMMWMMWWMK; ..;0NXc                 ")
print("             .oKXklcxXWW0c;;;lKWWKoco0XKl.                 ")
print("               'lx0NWWWWXkoloONWWWNN0xl'                   ")
print("      ':,..'.     .';cldXNXKXN0occ;'.     .'..,;.          ")
print("   .ldONX00XO:.         ;l:,cl.         .l0X00NXxo:.       ")
print("   .''cxllOOxkx;'cxxo:.         'ldxd;':kkx0kcod:..        ")
print("          .. .';OWWMMWKdc'. .,lkXWWWWNd,.. ..              ")
print("               .oNWMWMMMWNOdxO0KWMWWWK:                    ")
print("                 'cdxKNMMWMMWNKOOkxo:.                     ")
print("                  .;d00000XXNMMWN0l'.                      ")
print("               .,l0NXKOd;..',:lk0KXXkc.                    ")
print("               :xdc:'.          ..,:ldd'                   \n\n")

print ("(W)hois (A)SN (B)locklist (B)ulk (I)nquiry (T)ool\n")
print ("Now running IP ADDRESS lookups...")
print ("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")


try:
    targets = sys.argv[1]
except:
    print ("!!  ERROR   !!")
    sys.exit()

registrant_email_table = []
user_agent = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 Chrome/36.0.1985.125 Safari/537.36'}


def whois_lookup(ipaddr):
    try:
        obj = IPWhois(ipaddr)
        results = obj.lookup_whois()
        domain_asnid = "AS" + results['asn']
        if domain_asnid == "":
            domain_asnid = ""
        try:
            domain_country = results['asn_country_code']
            if domain_country == "":
                domain_country = "- -"    
        except:
            domain_country = "- -"
            pass
        try:
            domain_asn_name = results['nets'][0]['name']
            if domain_asn_name == "":
                domain_asn_name = "- -"
        except:
            domain_asn_name = "- -"
            pass
    except:
        pass
        domain_asnid = "- -"
        domain_country = "- -"
        domain_asn_name = "- -"
    #################### BLOCKLIST FUNCTION BELOW ##################
    try:
        url = "https://www.urlvoid.com/scan/" + ipaddr + "/"
        results = requests.get(url, headers=user_agent).content
        soup = BeautifulSoup(results, 'html.parser')
        t = soup.find('span',{'class':'label-danger'})
        urlvoid_bl = "URLVOID: " + t.text
        print(urlvoid_bl)
        #return urlvoid_bl
    except:
        urlvoid_bl = ""
        pass
    try:
        url2 = "https://fortiguard.com/webfilter?q=" + ipaddr + "&version=8"
        results2 = requests.get(url2, headers=user_agent).content
        soup2 = BeautifulSoup(results2, 'html.parser')
        t2 = soup2.find("meta", property="description")
        fortiguard = "FORTIGUARD " + str(t2["content"]) 
        print(fortiguard)
        #return fortiguard
    except:
        fortiguard = ""
        pass
    try:
        url3 = "http://www.siteadvisor.com/sitereport.html?url=" + ipaddr
        results3 = requests.get(url3, headers=user_agent).content
        soup3 = BeautifulSoup(results3, 'html.parser')
        t3 = soup3.find('a').contents[0]
        siteadvisor_bl = "SITEADVISOR: " + str(t3)
        print(siteadvisor_bl)
        #return fortiguard
    except:
        siteadvisor_bl = ""
        pass
    try:
        gsb_lookup = SafeBrowsing(gsb_apikey)
        results4 = gsb_lookup.lookup_urls([ipaddr])
        gsb_status = str(results4[ipaddr]['malicious'])
        gsb_platforms = results4[ipaddr]['platforms'][0]
        gsb_threats = results4[ipaddr]['threats'][0]
        print("GOOGLE SAFE BROWSING API4: " + gsb_status + " || " + gsb_platforms + " || " + gsb_threats)
    except:
        gsb_status = ""
        gsb_platforms = ""
        gsb_threats = ""
        pass
    try:
        url5 = "https://www.abuseipdb.com/check/" + ipaddr
        results5 = requests.get(url5, headers=user_agent).content
        soup5 = BeautifulSoup(results5, 'html.parser')
        abusedb_status = soup5.find_all('h3')[0].contents[2].strip().strip(" <tr>")
        if abusedb_status == "was found in our database!":
            abusedb_reported = soup5.find('div',{'class':'well'}).contents[3].contents[1].contents[0]
            abusedb_reported = str(abusedb_reported)
            abusedb_confidence = soup5.find('div',{'class':'well'}).contents[3].contents[3].contents[0]
            abusedb_confidence = str(abusedb_confidence)
            print("ABUSEDB : " + abusedb_status + " || " + abusedb_reported + " || " + abusedb_confidence)
        else:
            abusedb_status = ""
            abusedb_reported = ""
            abusedb_confidence = ""
    except:
        abusedb_status = ""
        abusedb_reported = ""
        abusedb_confidence = ""
        pass
    try:    
        output = ipaddr + ";" + domain_asnid + ";" + domain_asn_name + ";" + domain_country + ";" + gsb_status + ";" + gsb_platforms + ";" + gsb_threats + ";" + fortiguard + ";" + siteadvisor_bl + ";" + abusedb_status + ";" + abusedb_reported + ";" + abusedb_confidence + "\n"
    except:
        output = ipaddr + ";" + "error\n"
    filename1 =  "WABBIT4IP-LOOKUP-RESULTS.csv"
    with open (filename1, "a") as outputfile:
        outputfile.write(output)
    output = ""

inputfile = open(targets, "r")
all_ipaddrs = inputfile.readlines()
all_ipaddrs = set(all_ipaddrs)
inputfile.close()

for ipaddr in all_ipaddrs:
    ipaddr = ipaddr.strip("\n")
    print ("\n" + ipaddr + ":")
    whois_lookup(ipaddr)

print ("\n\n-=-=-=-=-   WABBIT HAS COMPLETED ALL IP LOOKUPS!  -=-=-=-=-\n\n")
    
sys.exit()

