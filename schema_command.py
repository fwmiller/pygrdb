from schema import *

def schema_command_add(argv, gno, cno):
	if len(argv) != 5:
		print('Illegal number of arguments for schema add')
		return

	if argv[2] != 'vertex' and argv[2] != 'v' and \
	   argv[2] != 'edge'   and argv[2] != 'e':
		print('Illegal schema type for schema add')
		return

	# Read existing schema
	schema = schema_read(gno, cno, argv[2])

	# Add new attribute to schema
	schema = schema_add(schema, argv[3], argv[4])

	# Write new schema
	schema_write(gno, cno, argv[2], schema)


def schema_command(argv, gno, cno):
	if len(argv) > 1:
		if argv[1] == 'add' or argv[1] == 'a':
			if gno < 0 or cno < 0:
				print('Component does not exist')
				return;

			schema_command_add(argv, gno, cno)
			return

	if gno >= 0 and cno >= 0:
		schema_print(gno, cno, 'v')
		schema_print(gno, cno, 'e')
