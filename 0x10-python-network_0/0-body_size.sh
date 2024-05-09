#!/bin/bash
# Takes in a url, sends a request and displays the body size
curl -sw "%{size_download}\n" -o /dev/null "$@"

