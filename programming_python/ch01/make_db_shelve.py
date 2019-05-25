from programming_python.ch01.initdata import bob, sue
import shelve

db = shelve.open('people-shelve')
db['bob'] = bob
db['sue'] = sue
db.close()
