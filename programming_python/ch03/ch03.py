import os

print(os.environ.keys())

print(list(os.environ.keys()))

print(os.environ['TMPDIR'])
print(os.environ['PYTHONPATH'])

for srcdir in os.environ['PYTHONPATH'].split(os.pathsep): print(srcdir)

import sys
print(sys.path[:3])

os.environ['TMPDIR'] = r'/tmp'
print(os.environ['TMPDIR'])

import sys
for f in (sys.stdin, sys.stdout, sys.stderr) : print(f)

# print('hello stdout world')
# input('hello stdout world>')

# print('hello stdout world>');sys.stdin.readline()[:-1]

from programming_python.ch03.streams.moreplus import more

more(open('/Users/wangjunchao/Project/python/programming_python/ch03/streams/adderSmall.py').read())