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
				valint = int(val)
				valuint = valint % 2**64
				b = bytearray(struct.pack('Q', valuint))
				vfd.write(b)
			elif attrtype == 'FLOAT':
				valfloat = float(val)
				b = bytearray(struct.pack('d', valfloat))
				vfd.write(b)
			elif attrtype == 'DOUBLE':
				valdouble = float(val)
				b = bytearray(struct.pack('d', valdouble))
				vfd.write(b)
			elif attrtype == 'CHAR':
				b = ord(val[0]).to_bytes(1, byteorder='little', signed=False)
				vfd.write(b)
			elif attrtype == 'STRING':
				b = bytearray()
				b.extend(map(ord, val))

				# Write string length
				blen = bytearray(struct.pack('H', len(b)))
				vfd.write(blen)

				# Write string padded out to max string length
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
