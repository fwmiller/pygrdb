import os
from config import GRDB_DIR

def graphs_get_list():
	glist = []
	rdir = os.path.expanduser(GRDB_DIR)
	dirs = os.listdir(rdir)
	for dir in dirs:
		glist.append(dir)
	return glist

def graphs_print():
	clist = []
	rdir = os.path.expanduser(GRDB_DIR)
	gdirs = os.listdir(rdir)
	for gdir in gdirs:
		cdirs = os.listdir(rdir + '/' + gdir)
		for cdir in cdirs:
			clist.append(''.join(gdir + '.' + cdir))
	for c in sorted(clist):
		print(c)

def graph_new():
	# Find highest existing graph number and add one
	glist = graphs_get_list()
	gnolist = list(map(int, glist))
	gno = max(gnolist or (-1)) + 1

	# Create directory for new graph
	rdir = os.path.expanduser(GRDB_DIR)
	os.mkdir(rdir + '/' + str(gno))

	# Create first component directory for new graph
	os.mkdir(rdir + '/' + str(gno) + '/0')

	# Create first vertex in the new component
