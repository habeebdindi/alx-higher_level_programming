#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.
curl -sI http://globallearna.tech | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r '
