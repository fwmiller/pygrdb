import struct

def read_attribute(attrtype, fd):
	if attrtype == 'INT':
		b = fd.read(8)
	elif attrtype == 'UINT':
		b = fd.read(8)
	elif attrtype == 'FLOAT':
		b = fd.read(8)
	elif attrtype == 'DOUBLE':
		b = fd.read(8)
	elif attrtype == 'CHAR':
		b = fd.read(1)
	elif attrtype == 'STRING':
		b = fd.read(2)
		len = struct.unpack('<H', b)[0]
		if len > 0:
			b = fd.read(256)
	elif attrtype == 'DATE':
		b = fd.read(10)
	elif attrtype == 'TIME':
		b = fd.read(8)


def read(s, fd):
	if not s:
		return

	# Iterate through the attributes of the schema and just read
	# the tuple data
	for attrtype, attrname in s:
		read_attribute(attrtype, fd)
