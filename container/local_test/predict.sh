#!/bin/bash

payload=$1
content=${2:-image/png}

curl --connect-timeout 600 --data-binary @${payload} -H "Content-Type: ${content}" -v http://localhost:8080/invocations
