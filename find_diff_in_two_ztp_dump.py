
file_a = 'a.txt'
file_b = 'b.txt'

da = dict()
db = dict()

with open(file_a, 'r') as fa:
    for line in fa:
        pos = line.find(',')
        line[:]
        da.setdefault(line, False)
print('%s parse finish...' % file_a)

with open(file_b, 'r') as fb:
    for line in fb:
        db.setdefault(line, False)
print('%s parse finish...' % file_b)

for key in da:
    if key in db:
        da[key] = True
        db[key] = True
print('compare finish...')
        
print('different items in %s' % file_a)
for key in da:
    if da[key]==False:
        print(key)
        
print('different items in %s' % file_b)
for key in db:
    if db[key]==False:
        print(key)