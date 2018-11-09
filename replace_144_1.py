file = 'smp-10.xml'
new_bsz = '--bsz (1,1),(1,1),(1,1) '
with open(file) as f:
    str_file = f.read()
    start_pos = str_file.find('--bsz')
    end_pos = str_file.find('--', start_pos+1)
    str_file = str_file.replace(str_file[start_pos:end_pos], new_bsz)
    print str_file