import xml.etree.ElementTree as ET

tree = ET.parse('country_data.xml')
root = tree.getroot()

first = list(root)[0]
print(first.attrib)
ET.dump(root)

print('-------')

ns = {'ns':'zte.com'}
cts = tree.findall('ns:country', ns)
for ct in cts:
    print(ct.tag)
