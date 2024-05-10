#!/usr/bin/python3
"""
Taing a URL, sends a request to URL and displaying the value of the
X-Request-Id variable found in the header of the response
"""
import sys
from urllib.request import urlopen

if __name__ == "__main__":
    url = sys.argv[1]
    with urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)
