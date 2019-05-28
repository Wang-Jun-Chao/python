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