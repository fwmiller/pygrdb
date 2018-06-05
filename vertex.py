import config

def new(cdir):
	# Create first vertex in the new component
	vfile = cdir + '/' + config.VERTEX_FILE
	try:
		vfd = open(vfile, 'ab')
	except:
		print('Open vertex file', vfile, 'failed')
		return False

	b = (1).to_bytes(8, byteorder='little', signed=False)
	vfd.write(b)
	vfd.close()

	return True


def add(cdir, vid):
	# Create a new edge file if it does not exist
	vfile = cdir + '/' + config.VERTEX_FILE
	try:
		vfd = open(vfile, 'ab')
	except:
		print('Write to file', vfile, 'failed')
		return

	# Add new vertex to vertex file
	b = (vid).to_bytes(8, byteorder='little', signed=False)
	vfd.write(b)
	vfd.close()


def exists(cdir, vid):
	vfile = cdir + '/' + config.VERTEX_FILE
	try:
		vfd = open(vfile, 'rb')
	except:
		print('Open vertex file', vfile, 'failed')
		return False

	while True:
		b = vfd.read(8)
		if not b:
			break

		i = int.from_bytes(b, byteorder='little', signed=False)
		if i == vid:
			vfd.close()
			return True

	vfd.close()
	return False
