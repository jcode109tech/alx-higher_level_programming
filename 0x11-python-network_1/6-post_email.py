#!/usr/bin/python3

"""
Takes in a URL and an email address, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
using the requests module
"""

if __name__ == "__main__":
    import requests
        from sys import argv

            response = requests.post(argv[1], data={"email": argv[2]})
                print(response.text)