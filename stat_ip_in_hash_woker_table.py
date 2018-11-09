def sortedDict(adict):
    keys = adict.keys()
    keys.sort()
    return map(adict.get, keys)

ipint2str = lambda x: '.'.join([str(x/(256**i)%256) for i in range(3,-1,-1)])
ipstr2int = lambda x:sum([256**j*int(i) for j,i in enumerate(x.split('.')[::-1])])

src_ip = dict()
dst_ip = dict()

i =0
with open('hash_key_value') as f:
    for line in f:
        i += 1
        # if i==8424720:
        if i==328:
            break
        ip  = int(line.split(',')[0], 16)
        dir = int(line.split(',')[1])
        if dir==1:
            src_ip.setdefault(ip, dir)
        elif dir ==0:
            dst_ip.setdefault(ip, dir)
            
            

print len(src_ip)            
for key in src_ip:
    print ipint2str(key)+'  '   ,

print '======='

print len(dst_ip)            
for key in dst_ip:
    print ipint2str(key)+'  '   ,

# keys = src_ip.items()
# keys.sort()
# for key in keys:
    # print ipint2str(key[0])

    
    
# keys = dst_ip.items()
# keys.sort()
# for key in keys:
    # print ipint2str(key[0])


