import os
import sys
from config import *

def graphs_get_list():
	glist = []
	rdir = os.path.expanduser(GRDB_DIR)
	dirs = os.listdir(rdir)
	for dir in dirs:
		glist.append(dir)
	return glist


def graph_print(gidx, cidx):
	rdir = os.path.expanduser(GRDB_DIR)
	gdir = rdir + '/' + gidx
	cdir = gdir + '/' + cidx

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

def graphs_print():
	#
	# Create a sorted list of all graphs with all there components
	# in gno.cno format
	#
	clist = []
	rdir = os.path.expanduser(GRDB_DIR)
	gdirs = os.listdir(rdir)
	for gdir in gdirs:
		cdirs = os.listdir(rdir + '/' + gdir)
		for cdir in cdirs:
			clist.append(''.join(gdir + '.' + cdir))

	# Print the contents of each graph and its components
	for c in sorted(clist):
		print(c + ': ', end='')
		print('(', end='')
		gidx, cidx = c.split('.')
		graph_print(gidx, cidx)
		print(')')


def graph_new():
	# Find highest existing graph number and add one
	gidx = 0
	glist = graphs_get_list()
	if glist:
		gidxlist = list(map(int, glist))
		gidx = max(gidxlist) + 1

	# Create directory for new graph
	rdir = os.path.expanduser(GRDB_DIR)
	gdir = rdir + '/' + str(gidx)
	os.mkdir(gdir)

	# Create first component directory for new graph
	cdir = gdir + '/0'
	os.mkdir(cdir)

	# Create first vertex in the new component
	vfile = cdir + '/' + VERTEX_FILE
	try:
		vfd = open(vfile, 'wb+')
	except:
		print('Write to file', vfile, 'failed')
		return (-1), (-1)

	bytes = (1).to_bytes(8, byteorder='little', signed=False)
	vfd.write(bytes)
	vfd.close()

	return gidx, 0
