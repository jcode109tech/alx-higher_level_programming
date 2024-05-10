#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status"""
from urllib.request import urlopen

with urlopen("https://alx-intranet.hbtn.io/status") as response:
    body = response.read()
    decoded_content = body.decode('utf-8')
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(decoded_content))

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
