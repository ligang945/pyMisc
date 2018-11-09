#!/usr/bin/python
import sys
import os
import time
def replace_in_file(old_str, new_str):
    file_name = 'ini/config/xdr_build.xml'
    str = open(file_name, 'r').read().replace(old_str, new_str)
    open(file_name, 'w').write(str)

replace_in_file('<!--lg', '')
n = int(sys.argv[1])+10
str1 = '<Stage%s/>' % n
str2 = '<Stage%s/><!--lg' % n
replace_in_file(str1, str2)
os.system('./stop_merge.sh')
os.system('./start_merge.sh')
