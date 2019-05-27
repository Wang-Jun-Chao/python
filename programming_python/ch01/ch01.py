bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 40000, 'hardware']
print((bob[0], sue[2]))  # 获取姓名，薪水
print(bob[0].split()[-1])  # Bob姓什么？
sue[2] *= 1.25
print(sue)

people = [bob, sue]  # 引用列表的列表
for person in people:
    print(person)

print(people[1][0])

for person in people:
    print(person[0].split()[-1])  # 打印姓氏
    person[2] *= 1.20  # 涨20%的薪水

for person in people: print(person[2])  # 检查新的薪酬

pays = [person[2] for person in people]  # 收集薪酬信息
print(pays)

pays = map((lambda x: x[2]), people)  # 同上(map是3.X 中的生成器）
print(list(pays))

people.append(['Toa', 50, 0, None])
print(len(people))
print(people[-1][0])

NAME, AGE, PAY = range(3)  # 0, 1和2
bob = ['Bob Smith', 42, 10000]
print(bob[NAME])
print((PAY, bob[PAY]))

bob = [['name', 'Bob Saith'], ['age', 42], ['pay', 10000]]
sue = [['name', 'Sue Jones'], ['age', 45], ['pay', 20000]]
people = [bob, sue]
for person in people:
    print(person[0][1], person[2][1])  # name, pay

names = [person[0][1] for person in people]  # 收集姓名
print(names)

for person in people:
    print(person[0][1].split()[-1])  # 获得姓
    person[2][1] *= 1.10  # 加10%的工资

for person in people: print(person[2])

for person in people:
    for (name, value) in person:
        if name == 'name':
            print(value)  # 寻找特定的字段


def field(record, label):
    for (fname, fvalue) in record:
        if fname == label:  # 根据名字寻找字段
            return fvalue


print(field(bob, 'name'))
print(field(sue, 'pay'))

for rec in people:
    print(field(rec, 'age'))  # 打印所有年龄

bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
print((bob['name'], sue['pay']))  # 既没有bob[0] 也没有sue[2]

print(bob['name'].split()[-1])

sue['pay'] *= 1.10
print(sue['pay'])

bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')
print(bob)
print(sue)

sue = {}
sue['name'] = 'Sue Jones'
sue['age'] = 45
sue['pay'] = 40000
sue['job'] = 'hdw'
print(sue)

names = ['name', 'age', 'pay', 'job']
values = ['Sue Jones', 45, 40000, 'hdw']
print(list(zip(names, values)))

sue = dict(zip(names, values))
print(sue)

fields = ('name', 'age', 'job', 'pay')
record = dict.fromkeys(fields, '?')
print(record)

print(bob)
print(sue)
people = [bob, sue]  # 引用列表
for person in people:
    print(person['name'], person['pay'], sep=', ')  # 所有的名字和薪水

for person in people:
    if person['name'] == 'Sue Jones':  # 获取sue的薪水
        print(person['pay'])

names = [person['name'] for person in people]  # 收集姓名
print(names)

names = list(map((lambda x: x['name']), people))  # 同上，生成式
print(names)

salary = sum(person['pay'] for person in people)  # 汇总薪水
print(salary)

result = [rec['name'] for rec in people if rec['age'] >= 45]  # 类似SQL查询
print(result)

result = [(rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people]
print(result)

G = (rec['name'] for rec in people if rec['age'] >= 45)
print(next(G))

G = ((rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people)
print(G.__next__())

for person in people:
    print(person['name'].split()[-1])  # 姓
    person['pay'] *= 1.10  # 加薪10%

for person in people: print(person['pay'])

bob2 = {'name': {'first': 'Bob', 'last': 'Smith'},
        'age': 42,
        'job': ['software', 'writing'],
        'pay': (40000, 50000)}

print(bob2['name'])  # bob的全名
print(bob2['name']['last'])  # bob的姓氏
print(bob2['pay'][1])  # bob的最高薪资

for job in bob2['job']: print(job)  # bob的所有工作

print(bob2['job'][-1])  # bob最近的工作
bob2['job'].append('janitor')  # bob得到一个新工作
print(bob2)

bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')
print(bob)

db = {}
db['bob'] = bob  # 引用字典的字典
db['sue'] = sue
print(db['bob']['name'])  # 获取bob的名字
db['sue']['pay'] = 50000  # 改变sue的薪水
print(db['sue']['pay'])  # 获取sue的薪水

print(db)

import pprint

pprint.pprint(db)

for key in db:
    print(key, '=>', db[key]['name'])

for key in db:
    print(key, '=>', db[key]['pay'])

for key in db:
    print(db[key]['name'].split()[-1])
    db[key]['pay'] *= 1.10

for record in db.values(): print(record['pay'])

x = [db[key]['name'] for key in db]
print(x)

x = [rec['name'] for rec in db.values()]
print(x)

db['tom'] = dict(name='Tom', age=50, job=None, pay=0)
print(db['tom'])
print(db['tom']['name'])
print(list(db.keys()))
print(len(db))
print([rec['age'] for rec in db.values()])
result = [rec['name'] for rec in db.values() if rec['age'] >= 45]
print(result)

import shelve

db = shelve.open('people-shelve')
bob = db['bob']
print(bob['name'].split()[-1])  # 获取bob的姓名
sue = db['sue']
sue['pay'] *= 1.25  # 给sue加薪
print(sue['pay'])

db['sue'] = sue
db.close()

from programming_python.ch01.person_start import Person

bob = Person('Bob Snttih ', 42)
sue = Person('Sue Jones', 45, 40000)

people = [bob, sue]  # 一个＂数据库＂列表
for person in people:
    print(person.name, person.pay)

x = [(person.name, person.pay) for person in people]
print(x)

result = [(rec.age ** 2 if rec.age >= 45 else rec.age) for rec in people]
print(result)

from programming_python.ch01.person import Person
from programming_python.ch01.manager import Manager

bob = Person(name='Bob Smith', age=42, pay=10000)
sue = Person(name='Sue Jones', age=45, pay=20000)
tom = Manager(name='Tom Doe', age=55, pay=30000)
db = [bob, sue, tom]
for obj in db:
    obj.giveRaise(.10)  # default or custom
for obj in db:
    print(obj.lastName(), '=>', obj.pay)

tom = Manager('Tom Jones', 50)
print(tom)  # prints: <Manager => Tom Jones>

from urllib.request import urlopen

conn = urlopen('http://localhost/cgi-bin/cgi101.py?user=Sue+Smith')
reply = conn.read()
result = reply
print(result)

result = urlopen('http://localhost/cgi-bin/cgi101.py').read()
print(result)
result = urlopen('http://localhost/cgi-bin/cgi101.py?user=Bob').read()
print(result)

D = {'say': 5, 'get': 'shrubbery'}
print(D['say'])

S = '%(say)s => %(get)s' % D
print(S)

D = {'say': 5, 'get': 'shrubbery'}
result = '%(say)s => %(get)s' % D
print(result)

from programming_python.ch01.person import Person

bob = Person('Bob', 35)

result = '%(name)s, %(age)s' % bob.__dict__
print(result)

result = '{0.name} => {0.age}'.format(bob)
print(result)

from urllib.request import urlopen

url = 'http://localhost/cgi-bin/peoplecgi.py?action=Fetch&key=sue'
result = urlopen(url).read()
print(result)

result = urlopen('http://localhost/cgi-bin/peoplecgi.py').read()
print(result)