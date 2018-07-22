import struct


def write_attribute(attrtype, fd):
	if attrtype == 'INT':
		b = bytearray(struct.pack('q', 0))
		fd.write(b)
	elif attrtype == 'UINT':
		b = bytearray(struct.pack('Q', 0))
		fd.write(b)
	elif attrtype == 'FLOAT':
		b = bytearray(struct.pack('d', 0.0))
		fd.write(b)
	elif attrtype == 'DOUBLE':
		b = bytearray(struct.pack('d', 0.0))
		fd.write(b)
	elif attrtype == 'CHAR':
		b = bytearray(struct.pack('c', b' '))
		fd.write(b)
	elif attrtype == 'STRING':
		b = bytearray(struct.pack('H', 0))
		fd.write(b)
	elif attrtype == 'DATE':
		fd.write(bytes('08-27-2016', 'utf-8'))
	elif attrtype == 'TIME':
		fd.write(bytes('00:00:00', 'utf-8'))


def write(s, fd):
	if not s:
		return

	# Iterate through the attributes of the schema and write an initial
	# value for the tuple data
	for attrtype, attrname in s:
		write_attribute(attrtype, fd)
