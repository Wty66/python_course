from __future__ import print_function
import fnmatch
import sys
import os


def analisize_apche(filename):
    d = {}
    with open(filename) as f:
        for l in f:
            code = l.strip().split(' ')[8]
            d.setdefault(code, 0)
            d[code] += 1

        errsum = 0
        allsum = 0
        for key, val in d.iteritems():
            if fnmatch.fnmatch(key, '4*'):
                errsum += val
            elif fnmatch.fnmatch(key, '5*'):
                errsum += val
            allsum += val

    percent = errsum * 1.0 / allsum * 100
    print('{0:.2f}%'.format(percent))


def main():
    sys.argv.append('')
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        raise SystemExit('{0} not exists'.format(filename))
    else:
        analisize_apche(filename)
    
if __name__ == '__main__':
    main()

