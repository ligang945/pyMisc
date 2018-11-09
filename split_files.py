import os
src_dir  = '/data2/yibiao/1214/stage_01'
dst_dirs = ['/data2/yibiao/1214/stage_01_1', '/data2/yibiao/1214/stage_01_2']


for dst_dir in dst_dirs:
    if not os.path.isdir(dst_dir):
        os.mkdir(dst_dir)

for parent, dirnames, filenames in os.walk(src_dir):
    pass

filenames.sort()

size = len(filenames)
i=0
index = 0
for filename in filenames:
    i += 1
    if i <= size/2:
        index = 0
    else:
        index = 1
    # print index,
    os.rename(os.path.join(parent, filename), os.path.join(dst_dirs[index], filename))
    # print os.path.join(parent, filename)
    # print os.path.join(dst_dirs[index], filename)
print('done!')