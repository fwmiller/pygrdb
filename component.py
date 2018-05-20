import os
from config import GRDB_DIR

def component_command(argv, gno):
	if len(argv) > 1:
		if argv[1] == 'new' or argv[1] == 'n':
			component_new(gno)
		return

	# Dump all components if no arguments
	components_print()

def components_get_list(gno):
	clist = []
	rdir = os.path.expanduser(GRDB_DIR)
	cdirs = os.listdir(rdir + '/' + str(gno))
	for cdir in cdirs:
		clist.append(cdir)
	return clist

def components_print():
	clist = []
	rdir = os.path.expanduser(GRDB_DIR)
	gdirs = os.listdir(rdir)
	for gdir in gdirs:
		cdirs = os.listdir(rdir + '/' + gdir)
		for cdir in cdirs:
			clist.append(''.join(gdir + '.' + cdir))
	for c in sorted(clist):
		print(c)

def component_new(gno):
	# Find highest existing component number for specified graph and
	# add one
	clist = components_get_list(gno)
	cnolist = list(map(int, clist))
	cno = max(cnolist or (-1)) + 1

	# Create directory for new component
	gdir = os.path.expanduser(GRDB_DIR) + '/' + str(gno)
	os.mkdir(gdir + '/' + str(cno))
