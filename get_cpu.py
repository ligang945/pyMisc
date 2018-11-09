log = 'xshell_screen.log'
merge_cnt = 1

#-------------------------------
record = 0
with open(log, 'r') as fl:
    for line in fl:
        if 'front_merge' in line:
            record += 1
# print(record)

#-------------------------------
avg_vm  = 0.0
avg_m   = 0.0
avg_cpu = 0.0
n = 0
with open(log, 'r') as fl:
    for line in fl:
        if 'front_merge' not in line:
            continue
        record -= 1
        if record >= 20:
            continue
        n += 1
        info = line.split()
        vm = info[4][:-1]
        m  = info[5][:-1]
        cpu= info[8]
        # print(vm, m, cpu)
        avg_vm = avg_vm*1.0*(n-1)/n + float(vm)*1.0/n
        avg_m = avg_m*1.0*(n-1)/n + float(m)*1.0/n
        avg_cpu = avg_cpu*1.0*(n-1)/n + float(cpu)*1.0/n

print('vm:%.2f, m:%.2f, cpu:%.2f' % (avg_vm/1000*merge_cnt, avg_m*merge_cnt, avg_cpu*merge_cnt))
