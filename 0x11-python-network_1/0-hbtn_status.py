#!/usr/bin/python3
""" script that fetches a https://alx-intranet.hbtn.io/status"""

import urllib.request

try:
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        body = response.read()
        utf8_content = body.decode('utf-8')

        print("Body response:")
        print("    - type:", type(body))
        print("    - content:", body)
        print("    - utf8 content:", utf8_content)
except Exception as e:
    print("Error:", e)