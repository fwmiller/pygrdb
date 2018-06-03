import config
import component
import component_print
import os
import vertex

def graphs_get_list():
	glist = []
	rdir = os.path.expanduser(config.GRDB_DIR)
	dirs = os.listdir(rdir)
	for dir in dirs:
		glist.append(dir)
	return glist


def graphs_print():
	#
	# Create a sorted list of all graphs with all there components
	# in gno.cno format
	#
	clist = []
	rdir = os.path.expanduser(config.GRDB_DIR)
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
		component_print.component_print(gidx, cidx)
		print(')')


def graph_new():
	# Find highest existing graph number and add one
	gidx = 0
	glist = graphs_get_list()
	if glist:
		gidxlist = list(map(int, glist))
		gidx = max(gidxlist) + 1

	# Create directory for new graph
	rdir = os.path.expanduser(config.GRDB_DIR)
	gdir = rdir + '/' + str(gidx)
	os.mkdir(gdir)

	# Create first component directory for new graph
	cdir = gdir + '/0'
	os.mkdir(cdir)

	# Create first vertex in the new component
	if not vertex.vertex_new(cdir):
		return (-1), (-1)

	return gidx, 0
