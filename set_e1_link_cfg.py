file_in = 'e1_link_stat.csv'
file_ot = 'e1_link_cfg.csv'

f_in = open(file_in, 'r')
f_ot = open(file_ot, 'a')
for line in f_in:
    linkid = line.split(',')[1]
    sp1 = line.split(',')[6]
    sp2 = line.split(',')[8]
    ip = line.split(',')[4]
    # print(linkid)
    # print(sp1)
    # print(sp2)
    s = linkid + ',0,'+sp1+','+sp2+',0,1,2,1,2,'+ ip + '\n'
    f_ot.write(s)

f_in.close()
f_ot.close()
print('done')
