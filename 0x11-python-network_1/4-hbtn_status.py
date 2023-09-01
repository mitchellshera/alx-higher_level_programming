#!/usr/bin/python3

import requests

url = 'https://alx-intranet.hbtn.io/status'

try:
    response = requests.get(url)
    response.raise_for_status()

    content = response.text

    print("Body response:")
    print("    - type:", type(content))
    print("    - content:", content)
except requests.exceptions.RequestException as e:
    print("Error:", e)
