#!/usr/bin/python3

"""
script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a
parameter, and finally displays the body of the response.
"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    request = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
