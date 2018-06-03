import component
import config
import os

def get_list():
	glist = []
	rdir = os.path.expanduser(config.GRDB_DIR)
	dirs = os.listdir(rdir)
	for dir in dirs:
		glist.append(dir)
	return glist


def dump():
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
		component.dump(gidx, cidx)
		print(')')
