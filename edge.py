import config

def add(cdir, vid1, vid2):
	# Create a new edge file if it does not exist
	efile = cdir + '/' + config.EDGE_FILE
	try:
		efd = open(efile, 'wb+')
	except:
		print('Write to file', efile, 'failed')
		return

	# Add new edge to edge file
	bytes1 = (vid1).to_bytes(8, byteorder='little', signed=False)
	bytes2 = (vid2).to_bytes(8, byteorder='little', signed=False)
	efd.write(bytes1)
	efd.write(bytes2)
	efd.close()
