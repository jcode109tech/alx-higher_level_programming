#!/usr/bin/python

"""
Takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""

if __name__ == "__main__":
        from urllib import request
                from sys import argv

                        with request.\
                                        urlopen(argv[1]) as response:
                                                        print(response.headers.get("X-Request-Id")) I 