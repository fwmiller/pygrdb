import os
from component import *
from vertex import *

def edge_command(argv, gno, cno):
	if len(argv) != 3:
		return

	if gno < 0 or cno < 0:
		print('Create a new graph first')
		return

	print('Add edge (' + argv[1] + ',' + argv[2] + ')')
	vid1 = int(argv[1])
	vid2 = int(argv[2])

	# Check whether one of the vertices is already in current component
	cdir = component_get_dir(gno, cno)
	if not vertex_exists(cdir, vid1) and \
	   not vertex_exists(cdir, vid2):
		print('At least one vertex must exist in current component')
		return

	# Check whether edge exists in current component

	# Add edge to current component
