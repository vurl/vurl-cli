import re
from os.path import join, dirname

from setuptools import setup


# reading package's version (same way sqlalchemy does)
with open(join(dirname(__file__), 'vurlcli.py')) as f:
    version = re.match('.*__version__ = \'(.*?)\'', f.read(), re.S).group(1)


dependencies = [
    'easycli',
    'requests',
]


setup(
    name='vurl-cli',
    version=version,
    description='vURL.ir shortener CLI',
    long_description=open('README.md').read(),
    install_requires=dependencies,
    py_modules=['vurl'],
    entry_points=dict(console_scripts='vurl=vurlcli:VURL.quickstart'),
    license='MIT',
)

