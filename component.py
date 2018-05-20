import os
from config import GRDB_DIR

def component_command(argv):
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
