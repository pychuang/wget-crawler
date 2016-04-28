#!/usr/bin/env python3

import argparse
import json
import lxml.etree
import requests
import sys

def main(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            print("%s\t%d" % (url, r.status_code))
            exit(1)
    except requests.exceptions.ConnectionError:
        print("%s\tConnectionError" % url)
    except requests.exceptions.TooManyRedirects:
        print("%s\tTooManyRedirects" % url)
    except requests.exceptions.Timeout:
        print("%s\tTimeout" % url)
    except requests.exceptions.HTTPError:
        print("%s\tHTTPError" % url)
    except requests.exceptions.RequestException:
        print("%s\tRequestException" % url)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='check if an URL is alive')
    parser.add_argument('url', help='URL')

    args = parser.parse_args()
    main(args.url)
