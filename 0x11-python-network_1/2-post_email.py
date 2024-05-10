#!/usr/bin/python3

"""
Takes in a URL and an email address and
sends a POST request to the passed URL
"""

if __name__ == "__main__":
        from urllib import request, parse
                from sys import argv

                        data = parse.urlencode({"email": argv[2]}).encode()
                                with request.urlopen(argv[1], data) as response:
                                                print(response.read().decode("utf-8"))