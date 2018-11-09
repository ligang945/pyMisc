#!/usr/bin/python

txt_dir = '/home/TestData/DPI_DATA/guangzhou_LTE/DPI_test_data/2'
xml_dir = '/home/ligang/xml'
xml_template = '/home/test_template.xml'
exclude = ['pcapstc.txt', 'badfile.txt']

#------------------------------------------------------------------------------------------

import os

#find all txt files
txt_files = []
if not os.path.exists(txt_dir):
    print('ERROR: %s not exist!' % txt_dir)
    exit()
for file in os.listdir(txt_dir):
    full_name = os.path.join(txt_dir, file)
    if os.path.isfile(full_name) and file.split('.')[-1] == 'txt' and file not in exclude:
        txt_files.append(full_name)
txt_files.sort()
print('INFO: find %d txt files in %s' % (len(txt_files), txt_dir))

#read all txt files
all_data = {}
for txt in txt_files:
    try:
        with open(txt) as f:
            lines = f.readlines()[4:]
            all_data.setdefault(txt, lines)
    except:
        print('ERROR: read %s fail' % txt)
        continue

#generate xml files
#it's hard to parse as xml file because of gb2312 and hanzi
if not os.path.exists(xml_dir):
    os.mkdir(xml_dir)

with open(xml_template) as template:
	template_content = template.read()

for key in all_data:
    file = os.path.split(key)[-1]
    short_name = file.split('.')[0].split('_')
    service_type = short_name[0]
    short_name.remove(service_type)
    lines = all_data[key]
    print('%s' % file)
    for i in range(0, len(lines)):
        try:
            words = lines[i].split()
            xml_file_name = service_type + '_' + words[3] + '_' + '_'.join(short_name) + '_' + str(i+1)  + '.xml'
            xml_file_fullname = os.path.join(xml_dir, xml_file_name)
            with open(xml_file_fullname, 'w') as xml_file:
                template_content_copy = template_content
                template_content_copy = template_content_copy.replace('template_datasource', file.split('.')[0])
                template_content_copy = template_content_copy.replace('template_sgsndataip', words[0])
                template_content_copy = template_content_copy.replace('template_ggsndataip', words[1])
                template_content_copy = template_content_copy.replace('template_srcip', words[2])
                template_content_copy = template_content_copy.replace('template_dstip', words[3])
                template_content_copy = template_content_copy.replace('template_val', words[6]+','+words[7]+','+words[8]+','+words[9])
                xml_file.write(template_content_copy)
                print('    %s' % xml_file_name)
        except:
            print('ERROR: %s format error' % file)
            break
            
print('INFO: finish generate xml files in %s' % xml_dir)
