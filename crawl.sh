#!/bin/sh

cat urls.txt | xargs -n 1 -P 48  wget --recursive --level 1 --wait 10 --random-wait -A htm,html,shtml --directory-prefix data
