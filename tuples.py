import component
import os
import schema
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
			b = fd.read(4)
			if not b:
				break
			if not first:
				print(',', end='')
			first = False
			f = struct.unpack('f', b)[0]
			print(f, end='')

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
			s = str(b)
			print(s, end='')

		elif attrtype == 'STRING':
			b = fd.read(2)
			len = struct.unpack('<H', b)[0]
			b = fd.read(len)
			if not b:
				break
			if not first:
				print(',', end='')
			first = False
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


def update_tuple(s, fd1, fd2):
	if not s:
		return

	count = 1
	# Iterate through all the attributes of the schema except the
	# last one and copy the tuple data to the new file one by one
	for attrtype, attrname in s:
		if count == len(s):
			break

		if attrtype == 'INT' or \
		   attrtype == 'UINT' or \
		   attrtype == 'DOUBLE':
			fd2.write(fd1.read(8))

		elif attrtype == 'FLOAT':
			fd2.write(fd1.read(4))

		count += 1

	# Add the new data for the last attribute of the schema to the
	# new file
	if attrtype == 'INT':
		b = bytearray(struct.pack('q', 0))
		fd2.write(b)
	elif attrtype == 'UINT':
		b = bytearray(struct.pack('Q', 0))
		fd2.write(b)
	elif attrtype == 'FLOAT':
		b = bytearray(struct.pack('f', 0.0))
		fd2.write(b)
	elif attrtype == 'DOUBLE':
		b = bytearray(struct.pack('d', 0.0))
		fd2.write(b)

'''
		elif attrtype == 'CHAR':
			if sprev:
				b = fd1.read(1)
				if not b:
					b = (0).to_bytes(1, byteorder='little')
			else:
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
'''

def update_vertexes(gno, cno, sv):
	vfile = component.get_dir(gno, cno) + '/v'
	fd1 = open(vfile, 'rb')
	fd2 = open(vfile + '.tmp', 'wb+')

	while True:
		vb = fd1.read(8)
		if not vb:
			break
		fd2.write(vb)
		update_tuple(sv, fd1, fd2)

	fd2.close()
	fd1.close()

	os.rename(vfile, vfile + '.bak')
	os.rename(vfile + '.tmp', vfile)


def update_edges(gno, cno, se):
	efile = component.get_dir(gno, cno) + '/e'
	fd1 = open(efile, 'rb')
	fd2 = open(efile + '.tmp', 'wb+')

	while True:
		v1b = fd1.read(8)
		if not v1b:
			break
		v2b = fd1.read(8)
		if not v2b:
			break
		fd2.write(v1b)
		fd2.write(v2b)
		update_tuple(se, fd1, fd2)

	fd2.close()
	fd1.close()

	os.rename(efile, efile + '.bak')
	os.rename(efile + '.tmp', efile)

	# XXX Remove old edge file backup
