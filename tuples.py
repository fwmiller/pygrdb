import struct

def dump(s, fd):
	if not s:
		return

	# Iterate through the attributes of the schema and print the values
	# associated with the current tuple
	first = True
	print('[', end='')

	for attrtype, attrname in s:
		if attrtype == 'INT':
			b = fd.read(8)
			if not b:
				break
			if not first:
				print(',', end='')
			first = False
			print(struct.unpack('<q', b)[0], end='')

		elif attrtype == 'UINT':
			b = fd.read(8)
			if not b:
				break
			if not first:
				print(',', end='')
			first = False
			print(struct.unpack('<Q', b)[0], end='')

		elif attrtype == 'FLOAT':
			b = fd.read(8)
			if not b:
				break
			if not first:
				print(',', end='')
			first = False
			d = struct.unpack('d', b)[0]
			print(d, end='')

		elif attrtype == 'DOUBLE':
			b = fd.read(8)
			if not b:
				break
			if not first:
				print(',', end='')
			first = False
			d = struct.unpack('d', b)[0]
			print(d, end='')

		elif attrtype == 'CHAR':
			b = fd.read(1)
			if not b:
				break
			if not first:
				print(',', end='')
			first = False
			print(str(b), end='')

		elif attrtype == 'STRING':
			b = fd.read(2)
			len = struct.unpack('<H', b)[0]
			if len > 0:
				b = fd.read(len)
				if not b:
					break
			if not first:
				print(',', end='')
			first = False
			if len == 0:
				print('\'\'', end='')
			else:
				s = str(b)
				print(s, end='')

		elif attrtype == 'DATE':
			b = fd.read(10)
			if not b:
				break
			if not first:
				print(',', end='')
			first = False
			s = str(b)
			print(s, end='')

		elif attrtype == 'TIME':
			b = fd.read(8)
			if not b:
				break
			if not first:
				print(',', end='')
			first = False
			s = str(b)
			print(s, end='')

	print(']', end='')
