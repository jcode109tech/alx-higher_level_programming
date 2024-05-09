#!/bin/bash
# Will display all methods that a server accepts
curl -sI -X OPTIONS "$1" | awk -F ': ' '/Allow/ {print $2}'

