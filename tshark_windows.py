#!/usr/bin/python
# example: tshark -R (gsm_map.dialogue.destinationReference) -w 124.cap -r \\10.9.29.108\FSRoot\dp10_data\GuangDongYD\GsmMap_GsmCap_E1\xili_data\124.cap

import os

# windows

filter   = 's1ap'
src_dir  = '\\\\10.9.29.100\\FSroot\\DX80\\dp10_data\\sc_lte\\ip_pure'
dst_dir  = '\\\\10.9.29.100\\FSroot\\DX80\\dp10_data\\sc_lte\\ip_pure_s1ap'

if not os.path.isdir(dst_dir):
    os.mkdir(dst_dir)

for parent, dirnames, filenames in os.walk(src_dir):
    pass
# for file in filenames:
    # if file.split('.')[-1] != 'pcap':
    # print file
filenames.sort()

f = open('cmd_s1ap.bat', 'w')
for filename in filenames:
    cmd = 'tshark -R ' + filter + ' -w ' + os.path.join(dst_dir, filename) + ' -r ' + os.path.join(parent, filename)+'\n'
    f.write(cmd)
f.close()


print('done!')