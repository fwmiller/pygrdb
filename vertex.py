import config
import schema
import tuples_read

def new(cdir):
	# Create first vertex in the new component
	vfile = cdir + '/' + config.VERTEX_FILE
	try:
		vfd = open(vfile, 'ab')
	except:
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
		return False

	sv = schema.read(cdir, 'v')
	while True:
		# Read the vertex id
		b = vfd.read(8)
		if not b:
			break

		i = int.from_bytes(b, byteorder='little', signed=False)
		if i == vid:
			vfd.close()
			return True

		# Skip over the tuple data if there is any
		if sv:
			tuples_read.read(sv, vfd)

	vfd.close()
	return False
