def dump(s, fd):
	# Iterate through the attributes of the schema and print the values
	# associated with the current tuple
    print('[', end='')
	for attrtype, attrname in s:
		if attrtype == 'INT':
			b = fd.read(8)
			if not b:
				break
			i = int.from_bytes(8, byteorder='little', signed=True)
			print(i, end='')

		elif attrtype == 'UINT':
			b = fd1.read(8)
			if not b:
				break
			u = int.from_bytes(8, byteorder='little', signed=False)
			print(u, end='')

		elif attrtype == 'FLOAT':
			b = fd1.read(4)
			if not b:
				break
			f = struct.unpack('f', b)
			print(f, end='')

		elif attrtype == 'DOUBLE':
			b = fd1.read(8)
			if not b:
				break
			print(d, end='')

		elif attrtype == 'CHAR':
			b = fd1.read(1)
			if not b:
				break
			s = str(b)
			print(s, end='')

		elif attrtype == 'STRING':
			b = fd1.read(2)
			len = struct.unpack('<H', b)
			b = fd1.read(len)
			if not b:
				break
			s = str(b)
			print(s, end='')

		elif attrtype == 'DATE':
			b = fd1.read(10)
			if not b:
				break
			s = str(b)
			print(s, end='')

		elif attrtype == 'TIME':
			b = fd1.read(8)
			if not b:
				break
			s = str(b)
			print(s, end='')

    print(']', end='')
