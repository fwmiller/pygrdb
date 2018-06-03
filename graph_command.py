import graph
import graphs

def graph_command(argv, gno, cno):
	if len(argv) > 1:
		if argv[1] == 'new' or argv[1] == 'n':
			gidx, cidx = graph.new()
		if gno < 0 or cno < 0:
			if gidx >= 0 and cidx >= 0:
				return gidx, cidx
		return gno, cno

	# Dump all graphs if no arguments
	graphs.dump()
	return gno, cno
