import time
import sys
import urllib2
print "[+] Attempting to find Internet..."
print "[+] Finding requirements..."
for timeout in [1,5,10,15]:
    try:
        response=urllib2.urlopen('https://www.google.com',timeout=timeout)
        print "[+] Found!"
    except:
        print "[-] Not found!"
        sys.exit()
time.sleep(3)
print "Loading..."
time.sleep(0.6)
print "  12%"
time.sleep(0.4)
print "  18%"
time.sleep(0.1)
print "  25%"
time.sleep(0.3)
print "  36%"
time.sleep(0.4)
print "  41%"
time.sleep(0.5)
print "  57%"
time.sleep(0.6)
print "  59%"
time.sleep(0.1)
print "  67%"
time.sleep(0.4)
print "  74%"
time.sleep(0.7)
print "  89%"
time.sleep(0.4)
print "  93%"
time.sleep(0.5)
print "  99%"
time.sleep(1)
print "  100% - Done!"
