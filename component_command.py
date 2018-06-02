import os
from component import *

def component_command(argv, gno, cno):
	if len(argv) > 1:
		if argv[1] == 'new' or argv[1] == 'n':
			# Create a new component
			if gno < 0:
				print('Create a new graph first')
				return gno, cno

			component_new(gno)
			return gno, cno

		if re.match(r'\d+\.\d+', argv[1]):
			# Switch to a specified component

			# Check whether component exists
			gidx, cidx = argv[1].split('.')
			rdir = os.path.expanduser(GRDB_DIR)
			gdir = rdir + '/' + str(gidx)
			if os.path.isdir(gdir):
				cdir = gdir + '/' + str(cidx)
				if os.path.isdir(cdir):
					return int(gidx), int(cidx)

			print('Component', argv[1], 'does not exist')

		return gno, cno

	# Dump all components if no arguments
	components_print(gno)
	return gno, cno
