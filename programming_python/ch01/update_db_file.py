from programming_python.ch01.make_db_file import loadDbase, storeDbase

db = loadDbase()
db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'
storeDbase(db)
