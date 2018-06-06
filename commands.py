import component
import components
import config
import edge
import graph
import graphs
import os
import re
import schema
import vertex

def component_cmd(argv, gno, cno):
	if len(argv) > 1:
		if argv[1] == 'new' or argv[1] == 'n':
			# Create a new component
			if gno < 0:
				print('Create a new graph first')
				return gno, cno

			component.new(gno)
			return gno, cno

		if re.match(r'\d+\.\d+', argv[1]):
			# Switch to a specified component

			# Check whether component exists
			gidx, cidx = argv[1].split('.')
			rdir = os.path.expanduser(config.GRDB_DIR)
			gdir = rdir + '/' + str(gidx)
			if os.path.isdir(gdir):
				cdir = gdir + '/' + str(cidx)
				if os.path.isdir(cdir):
					return int(gidx), int(cidx)

			print('Component', argv[1], 'does not exist')

		return gno, cno

	# Dump current component if no arguments
	if gno > 0 and cno > 0:
		print(str(gno) + '.' + str(cno) + ': ' + '(', end='')
		component.dump(gno, gno)
		print(')')

	return gno, cno


def edge_cmd(argv, gno, cno):
	if len(argv) != 3:
		return

	if gno < 0 or cno < 0:
		print('Create a new graph first')
		return

	vid1 = int(argv[1])
	vid2 = int(argv[2])

	# Check whether edge exists in current component
	cdir = component.get_dir(gno, cno)
	if edge.exists(cdir, vid1, vid2):
		print('Edge (' + str(vid1) + ',' + str(vid2) + ') exists')
		return

	# Check whether one of the vertices is already in current component
	if not vertex.exists(cdir, vid1) and not vertex.exists(cdir, vid2):
		print('At least one vertex must exist in current component')
		return

	# Add the new vertex to the current component
	if not vertex.exists(cdir, vid1):
		vertex.add(cdir, vid1)
	elif not vertex.exists(cdir, vid2):
		vertex.add(cdir, vid2)

	# Add edge to current component
	edge.add(cdir, vid1, vid2)



def graph_cmd(argv, gno, cno):
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


def schema_add(argv, gno, cno):
	if len(argv) != 4:
		print('Illegal number of arguments for schema add')
		return

	if argv[1] == 'vertex' or argv[1] == 'v':
		sv = schema.schema_read(gno, cno, 'v')
		sv = schema.schema_add(sv, argv[2], argv[3])
		schema.schema_write(gno, cno, 'v', sv)

	elif argv[1] == 'edge' or argv[1] == 'e':
		se = schema.schema_read(gno, cno, 'e')
		se = schema.schema_add(se, argv[2], argv[3])
		schema.schema_write(gno, cno, 'e', se)


def schema_cmd(argv, gno, cno):
	if gno < 0 or cno < 0:
		print('Create a new graph first')
		return

	if len(argv) > 1:
		if argv[1] == 'vertex' or argv[1] == 'v' or \
		   argv[1] == 'edge' or argv[1] == 'e':
			if gno < 0 or cno < 0:
				print('Component does not exist')
				return;

			schema_add(argv, gno, cno)
			return

	if gno >= 0 and cno >= 0:
		# Print schemas for specified component
		schema.schema_print(gno, cno, 'v')
		schema.schema_print(gno, cno, 'e')
