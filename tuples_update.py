import component
import os
import struct

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

		elif attrtype == 'CHAR':
			fd2.write(fd1.read(1))

		elif attrtype == 'STRING':
			b = fd1.read(2)
			fd2.write(b)
			length = struct.unpack('<h', b)[0]
			if length > 0:
				fd2.write(fd1.read(length))

		elif attrtype == 'DATE':
			fd2.write(fd1.read(10))

		elif attrtype == 'TIME':
			fd2.write(fd1.read(8))

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
	elif attrtype == 'CHAR':
		b = bytearray(struct.pack('c', b' '))
		fd2.write(b)
	elif attrtype == 'STRING':
		b = bytearray(struct.pack('H', 0))
		fd2.write(b)
	elif attrtype == 'DATE':
		fd2.write(bytes('08-27-2016', 'utf-8'))
	elif attrtype == 'TIME':
		fd2.write(bytes('00:00:00', 'utf-8'))


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
	# XXX Remove old vertex file backup


def update_edges(gno, cno, se):
	efile = component.get_dir(gno, cno) + '/e'
	try:
		fd1 = open(efile, 'rb')
	except:
		return
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
