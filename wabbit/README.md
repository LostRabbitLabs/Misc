# wabbit
Python3 script that will perform a bulk Domain Whois & ASN Lookup along with Blocklist check based on provided list of domain names.

(W)hois (A)sn (B)locklist (B)ulk (I)nquiry (T)ool

     Language: Python 3
     Libraries: requests, sys, socket, python-whois, IPWhois, BeautifulSoup, json, pysafebrowsing
     Purpose: OSINT - Whois, ASN & Blocklist Checker


# Install
Follow the steps below to install 'wabbit'.

     git clone https://github.com/lostrabbitlabs/wabbit
     cd wabbit
     chmod 655 wabbit.py
     pip3 install python-whois
     pip3 install IPWhois
     pip3 install bs4
     pip3 install pysafebrowsing


# Usage
Simply provide a target file with one (1) domain name per line and run the script.

     ./wabbit.py targets.txt
     ./wabbit-ip.py targets.txt


SAMPLE targets.txt (NOTE: use IP ADDRESSES for wabbit-ip.py):

     example.com
     example2.com
     example3.com


# Output
When completed will create a CSV output file with the following information per domain:

     Domain Whois Lookup
     ASN/IPWhois Lookup
     Blocklist Lookup (URLVoid, SiteAdvisor, Fortiguard, and optionally Google Safe Browsing API v4)

# Bonus
In order to use the Google Safe Browsing API you need to modify the 'gsb_apikey' value in wabbit.py. More information about GSB API v4 below:

     https://developers.google.com/safe-browsing/v4/get-started


