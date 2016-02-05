import xml.etree.ElementTree as ET
import urllib
url = raw_input('Enter - ')
input = urllib.urlopen(url).read()

stuff = ET.fromstring(input)
lst = stuff.findall('count')
print 'count:', len(lst)
print "sum", sum(lst)
print lst
for item in lst:
    print 'Name', item.find('name').text
    print 'Id', item.find('id').text
    print 'Attribute', item.get("x")
