#!/shebang

"""
#log4sh

Usage:
  main.py <urls.txt>
  main.py -h | --help
  main.py -v | --version

Options:
  -h --help     Show this screen.
  -v --version     Show version.

"""

from os import system as exec
from os.path import isfile
from docopt import docopt
from stoyled import good, info, warn, bad, bold, rst


def scan(url):
    return exec(f'sudo nuclei -t log4j-detect.yaml -u {url}')


def main():
    args = docopt(__doc__, version="#log4sh_0.1a")
    if args['--help'] or args['--version']:
        exit(0)
    filename = args['<urls.txt>']
    if isfile(filename):
        urls = open(filename).read().strip().split('\n')
        for url in urls:
            print(info(f'Scanning -> {url}'))
            if not scan(url):
                print(bad('Something went wrong'))
    else:
        url = filename
        print(warn(f'Scanning -> {url}'))
        scan(url)


if __name__ == '__main__':
    main()
