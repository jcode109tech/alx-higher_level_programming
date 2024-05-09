#!/bin/bash
# Sends a post request with params
url=$1 email="test@gmail.com" subject="I will always be here for PLD" response=$(curl -s -X POST -d "email=$email&subject=$subject" "$url" -o response.txt) && { echo "POST params:"; echo "    email: $email"; echo "    subject: $subject"; echo ""; echo "Response body:"; cat response.txt; } && rm -f response.txt

