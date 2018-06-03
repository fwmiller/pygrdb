import config
import graphs
import os
import vertex


def new():
	# Find highest existing graph number and add one
	gidx = 0
	glist = graphs.get_list()
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
	if not vertex.new(cdir):
		return (-1), (-1)

	return gidx, 0
