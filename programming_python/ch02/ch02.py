import sys, os

result = len(dir(sys))
print(result)

result = len(dir(os))
print(result)

result = len(dir(os.path))
print(result)

import sys

result = dir(sys)
print(result)

result = sys.__doc__
print(result)

help(sys)

line = 'aaa\nbbb\nccc\n'
print(line.split('\n'))

print(line.splitlines())

mystr = 'xxxSPAMxxx'
print(mystr.find('SPAM'))

mystr = 'xxaaxxaa'
print(mystr.replace('aa', 'SPAM'))

mystr = 'xxxSPAMxxx'
print('SPAM' in mystr)
print('Ni' in mystr)
print(mystr.find('Ni'))

mystr = '\t Ni\n'
print(mystr.strip())
print(mystr.rstrip())

mystr = 'SHRUBBERY'
print(mystr.lower())

print(mystr.isalpha())
print(mystr.isdigit())

import string

print(string.ascii_lowercase)
print(string.whitespace)

mystr = 'aaa,bbb.ccc'
print(mystr.split(','))

mystr = 'a b\nc\nd'
print(mystr.split())

delim = 'NI'
print(delim.join(['aaa', 'bbb', 'ccc']))

chars = list('Lorreta')
print(chars)
chars.append('!')
print(''.join(chars))

mystr = 'xxaaxxaa'
print('SPAM'.join(mystr.split('aa')))

print((int("42"), eval("42")))
print((str(42), repr(42)))
print((("%d" % 42), "{:d}".format(42)))
print(("42" + str(1), int("42") + 1))

file = open("spam.txt", 'w')
print(file.write(('spam' * 5) + '\n'))
file.close()

file = open("spam.txt")
text = file.read()
print(text)

import sys

print((sys.platform, sys.maxsize, sys.version))

if sys.platform[:3] == 'win': print('hello windows')

print(sys.path)

sys.path.append(r'/mydir')
print(sys.path)

print(sys.modules)
print(list(sys.modules.keys()))
print(sys)
print(sys.modules['sys'])

try:
    raise IndexError
except:
    print(sys.exc_info())

import traceback, sys


def grail(x):
    raise TypeError('already got one')


# try:
#     grail('arthur')
# except:
#     exc_info = sys.exc_info()
#     print(exc_info[0])
#     print(exc_info[1])
#     traceback.print_tb(exc_info[2])


import os

print(dir(os))
print(dir(os.path))

print(os.getpid())

print(os.getcwd())

os.chdir(r'/usr')
print(os.getcwd())

print((os.pathsep, os.sep, os.pardir, os.curdir, os.linesep))

print(
    os.path.isdir(r'/usr'),
    os.path.isfile(r'/usr')
)

print(
    os.path.isdir(r'/Users/wangjunchao/Project/python/programming_python/ch02/ch02.py'),
    os.path.isfile(r'/Users/wangjunchao/Project/python/programming_python/ch02/ch02.py')
)

print(
    os.path.isdir(r'nonesuch'),
    os.path.isfile(r'nonesuch')
)

print(os.path.exists(r'/usr'))
print(os.path.exists(r'/nonesuch'))

print(os.path.getsize(r'/Users/wangjunchao/Project/python/programming_python/ch02/ch02.py'))

print(os.path.split(r'/Users/wangjunchao/Project/python/programming_python/ch02/ch02.py'))

print(os.path.join(r'/tmp', 'output.txt'))

name = r'/tmp/output.txt'
print((os.path.dirname(name), os.path.basename(name)))

print(os.sep)

pathname = r'/a/b/c/d.txt'
print(os.path.split(pathname))

print(os.sep.join(pathname.split(os.sep)))

print(os.path.join(*pathname.split(os.sep)))

os.chdir(r'/tmp')
print(os.getcwd())
print(os.path.abspath(''))

print(os.path.abspath('temp'))

print(os.path.abspath(r'PP4E/dev'))

print(os.path.abspath('.'))
print(os.path.abspath('..'))

print(os.path.abspath(r'../examples'))


print(os.path.abspath(r'/PP4thEd/chapters'))
print(os.path.abspath(r'/temp/spam.txt'))

import os
print(os.system('ls'))

print(open('/Users/wangjunchao/Project/python/programming_python/ch02/system/helloshell.py').read())

text = os.popen('cat /Users/wangjunchao/Project/python/programming_python/ch02/system/helloshell.py').read()
print(text)

listing = os.popen('ls').readlines()
print(listing)

result = os.system('python /Users/wangjunchao/Project/python/programming_python/ch02/system/helloshell.py')
print(result)

output = os.popen('python /Users/wangjunchao/Project/python/programming_python/ch02/system/helloshell.py').read()
print(output)

import subprocess
result = subprocess.call('cat /Users/wangjunchao/Project/python/programming_python/ch02/system/helloshell.py', shell=True)
print(result)

pipe = subprocess.Popen('python /Users/wangjunchao/Project/python/programming_python/ch02/system/helloshell.py', shell=True, stdout=subprocess.PIPE)
result = pipe.communicate()
print(result)
result = pipe.returncode
print(result)

pipe = subprocess.Popen('python /Users/wangjunchao/Project/python/programming_python/ch02/system/helloshell.py', shell=True, stdout=subprocess.PIPE)
result = pipe.stdout.read()
print(result)
result = pipe.wait()
print(result)

from subprocess import  Popen, PIPE
result = Popen('python /Users/wangjunchao/Project/python/programming_python/ch02/system/helloshell.py', shell=True, stdout=PIPE).communicate()[0]
print(result)

import os
result = os.popen('python /Users/wangjunchao/Project/python/programming_python/ch02/system/helloshell.py').read()
print(result)

import os
for line in os.popen('ls *.py'): print(line, end='')

I = os.popen('ls *.py')
I

#
# I = os.popen('ls *.py')
# I = iter(I)
# I.__next__()
# next(I)












