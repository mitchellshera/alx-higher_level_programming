#!/bin/bash
#Sends a POST request to a given URL.
curl -s POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
