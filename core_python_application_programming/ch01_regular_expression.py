import re

print("CASE 1>>>")
# 模式匹配字符串
m = re.match('foo', 'foo')
if m is not None:
    # 如果匹配成功，就输出匹配内容
    print(m.group())
# 确认返回的匹配对象
print(m)

print("CASE 2>>>")
# 模式并不能匹配字符串
m = re.match('foo', 'bar')
# （单行版本的 if 语句）
if m is not None: m.group()
print(m)

print("CASE 3>>>")
m = re.match('foo', 'food on the table')
print(m.group())

print("CASE 4>>>")
result = re.match('foo', 'food on the table').group()
print(result)

print("CASE 5>>>")
m = re.match('foo', 'seafood')
if m is not None: print(m.group())

print("CASE 6>>>")
m = re.search('foo', 'seafood') # 使用 search() 代替
if m is not None: print(m.group())

print("CASE 7>>>")
bt = 'bat|bet|bit' # 正则表达式模式: bat、bet、bit
m = re.match(bt, 'bat')  # 'bat' 是一个匹配
if m is not None: print(m.group())

print("CASE 8>>>")
m = re.match(bt, 'blt') # 对于 'blt' 没有匹配
if m is not None: print(m.group())

print("CASE 9>>>")
m = re.match(bt, 'He bit me!')  # 不能匹配字符串
if m is not None: print(m.group())

print("CASE 10>>>")
m = re.search(bt, 'He bit me!')  # 通过搜索查找 'bit'
if m is not None: print(m.group())

print("CASE 11>>>")
anyend = '.end'
m = re.match(anyend, 'bend') # 点号匹配 'b'
if m is not None: print(m.group())

print("CASE 12>>>")
m = re.match(anyend, 'end') # 不匹配任何字符
if m is not None: print(m.group())

print("CASE 13>>>")
m = re.match(anyend, '\nend') # 除了 \n 之外的任何字符
if m is not None: print(m.group())

print("CASE 14>>>")
m = re.search('.end', 'The end.')# 在搜索中匹配 ' '
if m is not None: print(m.group())

print("CASE 15>>>")
patt314 = '3.14' # 表示正则表达式的点号
pi_patt = '3\.14'  # 表示字面量的点号 (dec. point)
m = re.match(pi_patt, '3.14')  # 精确匹配
if m is not None: print(m.group())

print("CASE 15>>>")
m = re.match(patt314, '3014')  # 点号匹配'0'
if m is not None: print(m.group())

print("CASE 16>>>")
m = re.match(patt314, '3.14')  # 点号匹配 '.'
if m is not None: print(m.group())

print("CASE 17>>>")
m = re.match('[cr][23][dp][o2]', 'c3po')# 匹配 'c3po'
if m is not None: print(m.group())
m = re.match('[cr][23][dp][o2]', 'c2do')# 匹配 'c2do'
if m is not None: print(m.group())
m = re.match('r2d2|c3po', 'c2do')# 不匹配 'c2do'
if m is not None: print(m.group())
m = re.match('r2d2|c3po', 'r2d2')# 匹配 'r2d2'
if m is not None: print(m.group())

print("CASE 18>>>")
patt = '\w+@(\w+\.)?\w+\.com'
print(re.match(patt, 'nobody@xxx.com').group())
print(re.match(patt, 'nobody@www.xxx.com').group())
patt = '\w+@(\w+\.)*\w+\.com'
print(re.match(patt, 'nobody@www.xxx.yyy.zzz.com').group())
m = re.match('\w\w\w-\d\d\d', 'abc-123')
if m is not None: print(m.group())
m = re.match('\w\w\w-\d\d\d', 'abc-xyz')
if m is not None: print(m.group())
m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')

print(m.group()) # 完整匹配
print(m.group(1)) # 子组 1
print(m.group(2)) # 子组 2
print(m.group(2)) # 子组 2
m = re.match('ab', 'ab') # 没有子组
print(m.group()) # 完整匹配
print(m.groups()) # 所有子组
m = re.match('(ab)', 'ab') # 一个子组
print(m.group()) # 完整匹配
print(m.group(1)) # 子组 1
print(m.groups()) # 全部子组
m = re.match('(a)(b)', 'ab') # 两个子组
print(m.group()) # 完整匹配
print(m.group(1)) # 子组 1
print(m.group(2)) # 子组 2
print(m.groups()) # 所有子组
m = re.match('(a(b))', 'ab') # 两个子组
print(m.group()) # 完整匹配
print(m.group(1)) # 子组 1
print(m.group(2)) # 子组 2
print(m.groups()) # 所有子组


print("CASE >>>")
print("CASE >>>")
print("CASE >>>")
print("CASE >>>")
print("CASE >>>")
print("CASE >>>")
print("CASE >>>")
print("CASE >>>")
print("CASE >>>")
print("CASE >>>")
print("CASE >>>")
print("CASE >>>")
print("CASE >>>")
print("CASE >>>")

