def schema_print(gno, cno):
	return

def schema_new():
	return {}

def schema_add(schema, name, base_type):
	if not schema:
		schema = {}
	schema[name] = base_type
	return schema
