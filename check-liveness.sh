#!/bin/sh

cat urls.txt | xargs -n 1 -d '\n' -P 48 -I % sh -c './check-liveness.py "%" ; sleep 10' | tee dead.txt
