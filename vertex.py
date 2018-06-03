import config

def vertex_new(cdir):
	# Create first vertex in the new component
	vfile = cdir + '/' + config.VERTEX_FILE
	try:
		vfd = open(vfile, 'wb+')
	except:
		print('Write to file', vfile, 'failed')
		return False

	bytes = (1).to_bytes(8, byteorder='little', signed=False)
	vfd.write(bytes)
	vfd.close()

	return True

def vertex_exists(cdir, vid):
	return False
