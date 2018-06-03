import schema

def schema_command_add(argv, gno, cno):
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


def schema_command(argv, gno, cno):
	if len(argv) > 1:
		if argv[1] == 'vertex' or argv[1] == 'v' or \
		   argv[1] == 'edge' or argv[1] == 'e':
			if gno < 0 or cno < 0:
				print('Component does not exist')
				return;

			schema_command_add(argv, gno, cno)
			return

	if gno >= 0 and cno >= 0:
		# Print schemas for specified component
		schema.schema_print(gno, cno, 'v')
		schema.schema_print(gno, cno, 'e')
