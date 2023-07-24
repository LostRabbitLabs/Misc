# domaindoxer
Python3 script, using the google search library, to quickly gather information around a provided 'domain name'.

     Language: Python 3
     Libraries: os, sys, google
     Purpose: OSINT - Data Leak Detector & Info Harvester


# Install
Follow the steps below to install 'domaindoxer'.

     git clone https://github.com/lostrabbitlabs/domaindoxer
     cd domaindoxer
     chmod 655 domaindoxer.py
     pip3 install google


# Usage
Simply provide a domain name and run the script.

     ./domaindoxer.py example.com


NOTE: Google does not like it when you run this more than a handful of times per hour. Use correctly...and sparringly.


# Output
When completed will potentially provide URL results on the console in the following areas of interest:

     Exposed Authentication Info
     Observed Public Containers/Buckets
     Document Leakages
     Internal Info Disclosures
     Code Repositories
     OSINT / Pastebin scrape

# Bonus
Create PDF output of results (requires additional software):

     ./domaindoxer.py example.com | aha -b | wkhtmltopdf - example.com.pdf


