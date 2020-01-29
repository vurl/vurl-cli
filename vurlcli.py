import sys

from easycli import Root, Argument
import requests


__version__ = '0.2.0'


class VURL(Root):
    __help__ = 'vURL.ir command line interface'
    __arguments__ = [
        Argument(
            'url',
            nargs='?',
            help='long URL to shorten, stdin will be used if not given.'
        ),
        Argument('-v', '--version', action='store_true', help='Show version'),
    ]

    def __call__(self, args):
        if args.version:
            print(__version__)
            return

        url = args.url
        if not url:
            url = sys.stdin.read()

        resp = requests.post('https://vurl.ir/apiv1', data=dict(url=url))
        if resp.status_code != 201:
            print('Invalid response from server:', file=sys.stderr)
            print(resp.text, file=sys.stderr)
            return 1

        print(f'https://vurl.ir/{resp.text}')
