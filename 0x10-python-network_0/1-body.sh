#!/bin/bash
# Will display the body of a response only if 200 is the response
curl -Is "$1" | grep -w 'Content-Length' | cut -f2 -d' '
