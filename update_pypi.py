import os
import argparse

from lazyprop import __version__


parser = argparse.ArgumentParser()
parser.add_argument('-m', '--message', help='Release description', type=str)
args = parser.parse_args()

exitcode = os.system('nosetests -v')
if exitcode == 0:
    os.system('git tag %s -m "%s" -f' % (__version__, args.message))
    os.system('git push --tags origin master -f')
    os.system('python setup.py register -r pypi')
    os.system('python setup.py sdist upload -r pypi')
else:
    print('Tests failed.  You\'re not ready')