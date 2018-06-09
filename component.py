import components
import config
import os
import vertex


def get_dir(gno, cno):
	rdir = os.path.expanduser(config.GRDB_DIR)
	gdir = rdir + '/' + str(gno)
	cdir = gdir + '/' + str(cno)
	return cdir


def dump_vertexes(cdir):
	# Print vertex set
	vfile = cdir + '/' + config.VERTEX_FILE
	try:
		vfd = open(vfile, 'rb')
	except:
		print('{}', end='')
		return

	# XXX Assume no tuples for the moment
	print('{', end='')

	vb = vfd.read(8)
	while True:
		vid = int.from_bytes(vb, byteorder='little')
		print(str(vid), end='')

		vb = vfd.read(8)
		if not vb:
			break;

		print(',', end='')

	print('}', end='')
	vfd.close()


def dump_edges(cdir):
	efile = cdir + '/' + config.EDGE_FILE
	try:
		efd = open(efile, 'rb')
	except:
		print(',{}', end='')
		return

	# XXX Assume no tuples for the moment
	print(',{', end='')

	e1b = efd.read(8)
	if not e1b:
		efd.close()
		return;

	e2b = efd.read(8)
	if not e2b:
		efd.close()
		return;

	while True:
		eid1 = int.from_bytes(e1b, byteorder='little', signed=False)
		eid2 = int.from_bytes(e2b, byteorder='little', signed=False)
		print('(' + str(eid1) + ',' + str(eid2) + ')', end='')

		e1b = efd.read(8)
		if not e1b:
			break;

		e2b = efd.read(8)
		if not e2b:
			break;

		print(',', end='')

	print('}', end='')
	efd.close()


def dump(gidx, cidx):
	cdir = get_dir(gidx, cidx)
	dump_vertexes(cdir)
	dump_edges(cdir)


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
