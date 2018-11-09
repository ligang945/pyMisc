import os
import xml.etree.ElementTree as et

report_xml = 'report.xml'
out_txt = 'input_klocwork_report.txt'

strns = 'xmlns:kw="http://www.klocwork.com/inForce/report/1.0"'

def delallchinstr(str, ch):
    while True:
        pos = str.find(ch)
        if pos == -1:
            break
        str = str.replace(str[pos:pos+len(ch)], '')
    return str
    
if __name__ == '__main__':
    if not os.path.isfile(report_xml):
        print('ERROR: file %s not exist!' % report_xml)
        exit()
        
    with open(report_xml, 'r') as file_x:
        str = file_x.read()

    strNew = delallchinstr(str, strns)
    
    try:
        tree = et.ElementTree(et.fromstring(strNew))
    except:
        print('ERROR: parse %s fail.' % report_xml)
        exit()
        
    files = tree.findall('problem/file')
    codes = tree.findall('problem/code')
    urls  = tree.findall('problem/url')
    
    if (len(files)!=len(codes)) or (len(codes)!=len(urls)):
        print('ERROR: %s format error.' % report_xml)
        exit()
    
    with open(out_txt, 'w') as file_o:
        for i in range(len(files)):
            file_o.write('%s;%s;%s\n' % (files[i].text, codes[i].text, urls[i].text))
            
    print('convert %s to %s done!' % (report_xml, out_txt) )