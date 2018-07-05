import config
import vertex


def set_vertex(cdir, vid, sv, name):
	vfile = cdir + '/' + config.VERTEX_FILE
	try:
		vfd = open(vfile, 'rb')
	except:
		return

	# Search for the specified vertex id.  If found, the file pointer
	# is left at the beginning of the tuple data
	if vertex.find(cdir, vid, vfd):
		vfd.close()
		return

	# Search to the specified attribute name
	for attrtype, attrname in sv:
		if name == attrname:
			# Replace the value of the attribute

		else:
			if attrtype == 'INT' or \
			   attrtype == 'UINT' or \
			   attrtype == 'DOUBLE':
				vfd.read(8)

			elif attrtype == 'FLOAT':
				vfd.read(4)

			elif attrtype == 'CHAR':
				vfd.read(1)

			elif attrtype == 'STRING':
				b = vfd.read(2)
				length = struct.unpack('<h', b)[0]
				if length > 0:
					vfd.read(length)

			elif attrtype == 'DATE':
				vfd.read(10)

			elif attrtype == 'TIME':
				vfd.read(8)

	vfd.close()


def set_edge():
	return
