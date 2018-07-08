import component
import components
import config
import edge
import graph
import graphs
import os
import re
import schema
import tuples
import tuples_set
import tuples_update
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
	if gno >= 0 and cno >= 0:
		print(str(gno) + '.' + str(cno) + ': ' + '(', end='')
		component.dump(gno, cno)
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
	sv = schema.read(cdir, 'v')
	if not vertex.exists(cdir, vid1):
		vertex.add(cdir, vid1, sv)
	elif not vertex.exists(cdir, vid2):
		vertex.add(cdir, vid2, sv)

	# Add edge to current component
	se = schema.read(cdir, 'e')
	edge.add(cdir, vid1, vid2, se)



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
		cdir = component.get_dir(gno, cno)
		sv = schema.read(cdir, 'v')
		sv = schema.add(sv, argv[2], argv[3])
		schema.write(cdir, 'v', sv)
		tuples_update.update_vertexes(gno, cno, sv)

	elif argv[1] == 'edge' or argv[1] == 'e':
		cdir = component.get_dir(gno, cno)
		se = schema.read(cdir, 'e')
		se = schema.add(se, argv[2], argv[3])
		schema.write(cdir, 'e', se)
		tuples_update.update_edges(gno, cno, se)


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
		cdir = component.get_dir(gno, cno)
		schema.dump(cdir, 'v')
		schema.dump(cdir, 'e')


def tuple_cmd(argv, gno, cno):
	if len(argv) < 2:
		print('Not enough arguments')
		return

	if argv[1] == 'vertex' or argv[1] == 'v':
		if len(argv) != 5:
			print('Illegal number of arguments for tuples set vertex')
			return

		cdir = component.get_dir(gno, cno)
		sv = schema.read(cdir, 'v')
		vid = int(argv[2])
		tuples_set.set_vertex(cdir, vid, sv, argv[3], argv[4])
		return

	elif argv[1] == 'edge' or argv[1] == 'e':
		if len(argv) != 6:
			print('Illegal number of arguments for tuples set edge')
			return

		cdir = component.get_dir(gno, cno)
		se = schema.read(cdir, 'e')
		vid1 = int(argv[2])
		vid2 = int(argv[3])
		tuples_set.set_edge(cdir, vid1, vid2, se, argv[4], argv[5])
		return
