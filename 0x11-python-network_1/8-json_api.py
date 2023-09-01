#!/usr/bin/python3

"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}

    try:
        response = requests.post(url, data=data)
        json_response = response.json()

        if not json_response:
            print("No result")
        else:
            print("[{}] {}".format(json_response.get("id"),
                                   json_response.get("name")))
    except ValueError:
        print("Not a valid JSON")
    except requests.exceptions.RequestException as e:
        print("Error:", e)
