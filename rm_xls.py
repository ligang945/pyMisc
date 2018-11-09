import os

file_path = '/home/zxt2000/share_plat_standard/xdr_build/linux'

os.chdir(file_path)
print os.getcwd()
files = os.listdir(file_path)

for file in files:
    if os.path.splitext(file)[1]=='.xls':
        os.system('rm '+file)
        print 'rm ' ,file

print 'all xls files deleted!'