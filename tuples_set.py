import config
import struct
import tuples_read
import vertex


def set_vertex(cdir, vid, sv, name, val):
	vfile = cdir + '/' + config.VERTEX_FILE
	try:
		vfd = open(vfile, 'rb+')
	except:
		return

	# Search for the specified vertex id.  If found, the file pointer
	# is left at the beginning of the tuple data
	if not vertex.find(cdir, vid, vfd):
		vfd.close()
		return

	# Search to the specified attribute name
	for attrtype, attrname in sv:
		if name == attrname:
			# Replace the value of the attribute
			if attrtype == 'INT':
				valint = int(val)
				b = bytearray(struct.pack('q', valint))
				vfd.write(b)
			elif attrtype == 'UINT':
				b = bytearray(struct.pack('Q', val))
				vfd.write(b)
			elif attrtype == 'FLOAT':
				b = bytearray(struct.pack('f', val))
				vfd.write(b)
			elif attrtype == 'DOUBLE':
				b = bytearray(struct.pack('d', val))
				vfd.write(b)
			elif attrtype == 'CHAR':
				b = bytearray(struct.pack('c', val))
				vfd.write(b)
			elif attrtype == 'STRING':
				b = bytearray(struct.pack('H', val))
				vfd.write(b)
			elif attrtype == 'DATE':
				vfd.write(bytes(val, 'utf-8'))
			elif attrtype == 'TIME':
				vfd.write(bytes(val, 'utf-8'))

		else:
			tuples_read.read_attribute(attrtype, vfd)

	vfd.close()


def set_edge(cdir, vid1, vid2, se, name, val):
	return
