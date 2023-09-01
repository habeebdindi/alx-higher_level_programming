#!/bin/bash
# sends a DELETE request to the URL passed
curl -sX DELETE -i "$1" | tail -n1
