# interactive queries
import shelve

fieldnames = ('name', 'age', 'job', 'pay')

maxfield = max(len(f) for f in fieldnames)
db = shelve.open('class-shelve')

while True:
    key = input('\nKey? => ')  # 键或者空行，空行退出
    if not key: break
    try:
        record = db[key]  # 依据键获取记录，在控制台显示
    except:
        print('No such key "%s"!' % key)
    else:
        for field in fieldnames:
            print(field.ljust(maxfield), '=>', getattr(record, field))
