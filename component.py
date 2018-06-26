import components
import config
import os
import schema
import struct
import tuples
import vertex


def get_dir(gno, cno):
	rdir = os.path.expanduser(config.GRDB_DIR)
	gdir = rdir + '/' + str(gno)
	cdir = gdir + '/' + str(cno)
	return cdir


def dump_vertexes(sv, cdir):
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
		print(struct.unpack('<q', vb)[0], end='')
		tuples.dump(sv, vfd)

		vb = vfd.read(8)
		if not vb:
			break;

		print(',', end='')

	print('}', end='')
	vfd.close()


def dump_edges(se, cdir):
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
		eid1 = struct.unpack('<q', e1b)[0]
		eid2 = struct.unpack('<q', e2b)[0]
		print('(' + str(eid1) + ',' + str(eid2) + ')', end='')
		tuples.dump(se, efd)

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
	sv = schema.read(cdir, 'v')
	se = schema.read(cdir, 'e')
	dump_vertexes(sv, cdir)
	dump_edges(se, cdir)


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
