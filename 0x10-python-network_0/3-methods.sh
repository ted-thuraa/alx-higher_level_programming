#!/bin/bash
#  script that takes in a URL and displays all HTTP methods the server will accept
curl -s -i -X OPTIONS "$1" 2>$1 | grep "Allow" | cut -d " " -f 2-