#!/bin/sh

./readhp.py | xargs -n 1 -P 8  wget --recursive --level 1 --wait 10 --random-wait -A htm,html,shtml --directory-prefix data
