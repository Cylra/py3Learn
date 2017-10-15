#! /usr/bin/python3
import urllib.request
import urllib.error

try:
    urllib.request.urlopen("http://blog1.csdn.net")
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.reason)
except urllib.error.URLError as e:
    if hasattr(e, "code"):
        print(e.code)
    print(e.reason)