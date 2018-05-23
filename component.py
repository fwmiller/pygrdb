import os
import re
from config import GRDB_DIR

def components_get_list(gno):
	clist = []
	rdir = os.path.expanduser(GRDB_DIR)
	cdirs = os.listdir(rdir + '/' + str(gno))
	for cdir in cdirs:
		clist.append(cdir)
	return clist

def components_print(gno):
	clist = components_get_list(gno)
	for c in sorted(clist):
		print(str(gno) + '.' + c)

def component_new(gno):
	# Find highest existing component number for specified graph and
	# add one
	clist = components_get_list(gno)
	cnolist = list(map(int, clist))
	cno = max(cnolist or (-1)) + 1

	# Create directory for new component
	gdir = os.path.expanduser(GRDB_DIR) + '/' + str(gno)
	os.mkdir(gdir + '/' + str(cno))

	# Create first vertex in the new component
