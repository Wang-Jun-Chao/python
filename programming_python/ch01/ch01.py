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
