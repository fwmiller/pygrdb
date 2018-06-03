import components
import config
import os
import vertex


def get_dir(gno, cno):
	rdir = os.path.expanduser(config.GRDB_DIR)
	gdir = rdir + '/' + str(gno)
	cdir = gdir + '/' + str(cno)
	return cdir


def dump(gidx, cidx):
	cdir = get_dir(gidx, cidx)

	# Print vertex set
	vfile = cdir + '/' + config.VERTEX_FILE
	try:
		vfd = open(vfile, 'rb')
	except:
		print('Open', vfile, 'failed')
		return

	# XXX Assume no tuples for the moment
	print('{', end='')
	vidbytes = vfd.read(8)
	while vidbytes:
		vid = int.from_bytes(vidbytes, byteorder='little')
		print(str(vid), end='')
		vidbytes = vfd.read(8)
		if not vidbytes:
			break;
		print(',', end='')
	print('}', end='')
	vfd.close()

	# Print edge set
	efile = cdir + '/' + config.VERTEX_FILE
	try:
		efd = open(efile, 'rb')
	except:
		print('Open', efile, 'failed')
		return

	# XXX Assume no tuples for the moment
	print(',{', end='')
	eid1bytes = efd.read(8)
	eid2bytes = efd.read(8)
	while eid1bytes and eid2bytes:
		eid1 = int.from_bytes(eid1bytes, byteorder='little')
		eid2 = int.from_bytes(eid2bytes, byteorder='little')
		print('(' + str(eid1) + ',' + str(eid2) + ')', end='')
		eid1bytes = efd.read(8)
		eid2bytes = efd.read(8)
		if not eid1bytes or eid2bytes:
			break;
		print(',', end='')
	print('}', end='')
	efd.close()


def new(gno):
	# Find highest existing component number for specified graph and
	# add one
	clist = components.get_list(gno)
	cnolist = list(map(int, clist))
	cno = max(cnolist or (-1)) + 1

	# Create directory for new component
	cdir = get_dir(gno, cno)
	os.mkdir(cdir)

	# Create first vertex in the new component
	vertex.new(cdir)
