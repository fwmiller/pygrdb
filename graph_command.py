from graph import *

def graph_command(argv, gno, cno):
	if len(argv) > 1:
		if argv[1] == 'new' or argv[1] == 'n':
			gidx, cidx = graph_new()
		if gno < 0 or cno < 0:
			return gidx, cidx
		else:
			return gno, cno

	# Dump all graphs if no arguments
	graphs_print()
	return gno, cno
