#!/usr/bin/env python3

import pickle


def main():
    filename = 'homepages-list.pickle'
    data = None
    with open(filename, 'rb') as f:
        data = pickle.load(f, encoding='utf-8')

    for (gsid, name, homepage, interests) in data:
        print(homepage)


if __name__ == '__main__':
    main()
