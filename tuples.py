import component
import os
import schema


def update_vertex_tuples(gno, cno):
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

		# Iterate through the attributes of the schema and copy the tuple
		# data to the new file one by one
		for attrtype, attrname in sv:
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
					b = (0).to_bytes(4, byteorder='little')
				fd2.write(b)

			elif attrtype == 'DOUBLE':
				b = fd1.read(8)
				if not b:
					b = (0).to_bytes(8, byteorder='little')
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

	fd2.close()
	fd1.close()

	os.rename(vfile, vfile + '.bak')
	os.rename(vfile + '.tmp', vfile)

	# XXX Remove old vertex file backup
