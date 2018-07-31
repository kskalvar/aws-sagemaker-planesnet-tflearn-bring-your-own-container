#!/bin/bash

payload=$1
content=${2:-image/png}

#curl --data-binary @${payload} -H "Content-Type: ${content}" -v http://localhost:8080/invocations
curl --data-binary @${payload} -H "Content-Type: ${content}" -i http://localhost:8080/invocations