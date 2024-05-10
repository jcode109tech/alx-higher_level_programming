#!/usr/bin/python3

"""
Script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""

if __name__ == "__main__":
    import requests
        from sys import argv

            response = requests.get("https://api.github.com/user",
                                        auth=(argv[1], argv[2]))
                                            print(response.json().get("id"))