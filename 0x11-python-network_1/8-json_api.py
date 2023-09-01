#!/usr/bin/python3

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
            print("[{}] {}".format(json_response['id'], json_response['name']))
    except ValueError:
        print("Not a valid JSON")
    except requests.exceptions.RequestException as e:
        print("Error:", e)
