#!/bin/bash
#Write a Bash script that takes in a URL and displays all HTTP methods
curl -sI OPTIONS "$1" | grep -i "allow" | cut -d" " -f2-
