import component
import config
import os
import struct
import tuples_write


def update_tuple(s, fd1, fd2):
	if not s:
		return

	count = 1
	# Iterate through all the attributes of the schema except the
	# last one and copy the tuple data to the new file one by one
	for attrtype, attrname in s:
		if count == len(s):
			break

		if attrtype == 'INT':
			fd2.write(fd1.read(config.BASE_TYPE_SIZES['INT']))

		elif attrtype == 'UINT':
			fd2.write(fd1.read(config.BASE_TYPE_SIZES['UINT']))

		elif attrtype == 'FLOAT':
			fd2.write(fd1.read(config.BASE_TYPE_SIZES['FLOAT']))

		elif attrtype == 'DOUBLE':
			fd2.write(fd1.read(config.BASE_TYPE_SIZES['DOUBLE']))

		elif attrtype == 'CHAR':
			fd2.write(fd1.read(config.BASE_TYPE_SIZES['CHAR']))

		elif attrtype == 'STRING':
			b = fd1.read(2)
			fd2.write(b)

			if struct.unpack('<h', b)[0] > 0:
				fd2.write(fd1.read(config.BASE_TYPE_SIZES['STRING']))

		elif attrtype == 'DATE':
			fd2.write(fd1.read(config.BASE_TYPE_SIZES['DATE']))

		elif attrtype == 'TIME':
			fd2.write(fd1.read(config.BASE_TYPE_SIZES['TIME']))

		count += 1

	# Add the new data for the last attribute of the schema to the
	# new file
	tuples_write.write_attribute(attrtype, fd2)


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
