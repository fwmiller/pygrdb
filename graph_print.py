from component import *

def graph_print(gidx, cidx):
	cdir = component_get_dir(gidx, cidx)

	# Print vertex set
	vfile = cdir + '/' + VERTEX_FILE
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
	efile = cdir + '/' + VERTEX_FILE
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
