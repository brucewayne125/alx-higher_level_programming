#!/bin/bash
#Bash script that takes in a URL, sends a request to that URL
#!/bin/bash
curl -s -o /dev/null -w "%{size_download}" "$1"
