import config

def add(cdir, vid1, vid2):
	# Create a new edge file if it does not exist
	efile = cdir + '/' + config.EDGE_FILE
	try:
		efd = open(efile, 'ab')
	except:
		print('Write to file', efile, 'failed')
		return

	# Add new edge to edge file
	b1 = (vid1).to_bytes(8, byteorder='little', signed=False)
	b2 = (vid2).to_bytes(8, byteorder='little', signed=False)
	efd.write(b1)
	efd.write(b2)
	efd.close()

def exists(cdir, vid1, vid2):
	efile = cdir + '/' + config.EDGE_FILE
	try:
		efd = open(efile, 'rb')
	except:
		return False

	while True:
		b1 = efd.read(8)
		if not b1:
			break
		b2 = efd.read(8)
		if not b2:
			break

		i1 = int.from_bytes(b1, byteorder='little', signed=False)
		i2 = int.from_bytes(b2, byteorder='little', signed=False)
		if i1 == vid1 and i2 == vid2:
			efd.close()
			return True

	efd.close()
	return False
