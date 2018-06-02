from schema import *

def schema_command_vertex(argv, gno, cno):
	if len(argv) != 4:
		print('Illegal number of arguments for schema vertex add')
		return

	if argv[1] == 'vertex' or argv[1] == 'v':
		# Read existing vertex schema
		schema = schema_read(gno, cno, 'v')

		# Add new attribute to vertex schema
		schema = schema_add(schema, argv[2], argv[3])

		# Write new vertex schema
		schema_write(gno, cno, 'v', schema)


def schema_command(argv, gno, cno):
	if len(argv) > 1:
		if argv[1] == 'vertex' or argv[1] == 'v':
			if gno < 0 or cno < 0:
				print('Component does not exist')
				return;

			schema_command_vertex(argv, gno, cno)
			return

	if gno >= 0 and cno >= 0:
		# Print schemas for specified component
		schema_print(gno, cno, 'v')
		schema_print(gno, cno, 'e')
