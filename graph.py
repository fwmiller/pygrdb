import os
from config import GRDB_DIR

def graph_command(argv):
	if len(argv) > 1:
		if argv[1] == 'new' or argv[1] == 'n':
			graph_new()
		return

	# Dump all graphs if no arguments
	graphs_print()
	
def graphs_get_list():
	glist = []
	rdir = os.path.expanduser(GRDB_DIR)
	dirs = os.listdir(rdir)
	for dir in dirs:
		glist.append(dir)
	return glist

def graphs_print():
	glist = graphs_get_list()
	for g in sorted(glist):
		print(g)

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
