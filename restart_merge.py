
def replace_in_file(old_str, new_str):
    file_name = 'ini/config/xdr_build.xml'
    str = open(file_name, 'r').read().replace(old_str, new_str)
    open(file_name, 'w').write(str)

replace_in_file('<!--lg', '')
n = 10
str1 = '<Stage%s/>' % n
str1 = '<Stage%s/>\n<!--lg' % n
replace_in_file(str1, str2)
