import os
import re
from config import GRDB_DIR

def component_command(argv, gno, cno):
	if len(argv) > 1:
		if argv[1] == 'new' or argv[1] == 'n':
			component_new(gno)
			return gno, cno

		if component_spec_check_syntax(argv[1]):
			# Check whether component exists
			gidx, cidx = argv[1].split('.')
			rdir = os.path.expanduser(GRDB_DIR)
			gdir = rdir + '/' + str(gidx)
			if os.path.isdir(gdir):
				cdir = gdir + '/' + str(cidx)
				if os.path.isdir(cdir):
					return int(gidx), int(cidx)
			printf('Component', argv[1], 'does not exist')

		return gno, cno

	# Dump all components if no arguments
	components_print(gno)
	return gno, cno

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

def component_spec_check_syntax(cspec):
	if re.match(r'\d+\.\d+', cspec):
		return True
	else:
		return False
