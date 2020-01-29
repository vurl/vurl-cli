import sys

from easycli import Root, Argument
import requests


__version__ = '0.1.0'


class VURL(Root):
    __help__ = 'vURL.ir command line interface'
    __arguments__ = [
        Argument('url', help='long URL to shorten'),
        Argument('-v', '--version', action='store_true', help='Show version'),
    ]

    def __call__(self, args):
        if args.version:
            print(__version__)
            return

        resp = requests.post('https://vurl.ir/apiv1', data=dict(url=args.url))
        if resp.status_code != 201:
            print('Invalid response from server:', file=sys.stderr)
            print(resp.text, file=sys.stderr)
            return 1

        print(f'https://vurl.ir/{resp.text}')
