import component
import os
import schema
import struct


def update(s, fd1, fd2):
	# Iterate through the attributes of the schema and copy the tuple
	# data to the new file one by one
	for attrtype, attrname in s:
		if attrtype == 'INT':
			b = fd1.read(8)
			if not b:
				b = (0).to_bytes(8, byteorder='little', signed=True)
			fd2.write(b)

		elif attrtype == 'UINT':
			b = fd1.read(8)
			if not b:
				b = (0).to_bytes(8, byteorder='little', signed=False)
			fd2.write(b)

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


def update_vertexes(gno, cno):
	sv = schema.read(gno, cno, 'v')
	if not sv:
		return

	vfile = component.get_dir(gno, cno) + '/v'
	fd1 = open(vfile, 'rb')
	fd2 = open(vfile + '.tmp', 'wb+')

	while True:
		vb = fd1.read(8)
		if not vb:
			break
		fd2.write(vb)
		update(sv, fd1, fd2)

	fd2.close()
	fd1.close()

	os.rename(vfile, vfile + '.bak')
	os.rename(vfile + '.tmp', vfile)


def update_edges(gno, cno):
	se = schema.read(gno, cno, 'e')
	if not se:
		return

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
		update(se, fd1, fd2)

	fd2.close()
	fd1.close()

	os.rename(efile, efile + '.bak')
	os.rename(efile + '.tmp', efile)

	# XXX Remove old edge file backup
