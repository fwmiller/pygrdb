import struct

def read(s, fd):
	if not s:
		return

	# Iterate through the attributes of the schema and just read
	# the tuple data
	for attrtype, attrname in s:
		if attrtype == 'INT':
			b = fd.read(8)
			if not b:
				break

		elif attrtype == 'UINT':
			b = fd.read(8)
			if not b:
				break

		elif attrtype == 'FLOAT':
			b = fd.read(4)
			if not b:
				break

		elif attrtype == 'DOUBLE':
			b = fd.read(8)
			if not b:
				break

		elif attrtype == 'CHAR':
			b = fd.read(1)
			if not b:
				break

		elif attrtype == 'STRING':
			b = fd.read(2)
			len = struct.unpack('<H', b)[0]
			if len > 0:
				b = fd.read(len)
				if not b:
					break

		elif attrtype == 'DATE':
			b = fd.read(10)
			if not b:
				break

		elif attrtype == 'TIME':
			b = fd.read(8)
			if not b:
				break
