#!/usr/bin/python
# example: tshark -R (gsm_map.dialogue.destinationReference) -w 124.cap -r \\10.9.29.108\FSRoot\dp10_data\GuangDongYD\GsmMap_GsmCap_E1\xili_data\124.cap

import os


# linux

filter   = 's1ap||gtpv2||diameter'
src_dir  = '/home/genius/new_sc_lte'
dst_dir  = '/home/genius/new_sc_lte_pure'

if not os.path.isdir(dst_dir):
    os.mkdir(dst_dir)

for parent, dirnames, filenames in os.walk(src_dir):
    pass
# for file in filenames:
    # if file.split('.')[-1] != 'pcap':
    # print file
filenames.sort()

size = len(filenames)
i=0
for filename in filenames:
    cmd = 'tshark -R ' + filter + ' -w ' + os.path.join(dst_dir, filename) + ' -r ' + os.path.join(parent, filename)
    i += 1
    print "%d/%d:" % (i, size), cmd
    os.system(cmd)
print('done!')