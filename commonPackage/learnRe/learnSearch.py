import re
text = "JGood is a handsome boy, he is cool, clever, and so on..."
m = re.search(r'\shan(ds)ome\s', text)
if m:
	print type(m)
	print m.group()
	print m.group(0), m.group(1)
else:
	print 'not search' 
