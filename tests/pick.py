import pickledb
db = pickledb.load('example.db', False)
# db.set('key', 'value')
print(db.get('key'))
db.dump()