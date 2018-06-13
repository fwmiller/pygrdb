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
b = bytearray(struct.pack('f', 0.0))
fd2.write(b)

elif attrtype == 'DOUBLE':
b = fd1.read(8)
if not b:
b = bytearray(struct.pack('d', 0.0))
fd2.write(b)

elif attrtype == 'CHAR':
b = fd1.read(1)
if not b:
b = (0).to_bytes(1, byteorder='little')
fd2.write(b)

elif attrtype == 'STRING':
b = fd1.read(2)
if not b:
b = (0).to_bytes(2, byteorder='little', signed=False)
fd2.write(b)
else:
fd2.write(b)
len = int.from_bytes(b, byteorder='little', signed=False)
b = fd1.read(len)
if b:
fd2.write(b)

elif attrtype == 'DATE':
b = fd1.read(10)
if not b:
b = (0).to_bytes(10, byteorder='little')
fd2.write(b)

elif attrtype == 'TIME':
b = fd1.read(8)
if not b:
b = (0).to_bytes(8, byteorder='little')
fd2.write(b)

    print(']', end='')
