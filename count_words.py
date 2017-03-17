from __future__ import print_function
import os
import sys


def count_word(filename):
    d = {}
    with open(filename) as f:
    
        for l in f:
            for w in l.strip().split(':'):
                d.setdefault(w, 0)
                d[w] += 1

    for key, val in d.iteritems():
        print(key, ':', val)


def main():
    sys.argv.append('')
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        raise SystemExit('{0} not found'.format(filename))
    else:
        count_word(filename)
        
if __name__ == '__main__':
    main()

