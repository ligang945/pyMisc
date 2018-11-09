import os

file = 'perf.log'

with open(file) as f:
    for line in f:
        if 'libdecode.so' in line:
            cmd = 'c++filt %s' %  line.split()[2]
            os.system(cmd)
