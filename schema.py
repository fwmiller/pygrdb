import config
import json
import os


def filename(gno, cno, schema_type):
	fname = os.path.expanduser(config.GRDB_DIR)
	fname += '/' + str(gno)
	fname += '/' + str(cno)
	if schema_type == 'vertex' or schema_type == 'v':
		fname += '/' + config.VERTEX_SCHEMA_FILE
	elif schema_type == 'edge' or schema_type == 'e':
		fname += '/' + config.EDGE_SCHEMA_FILE
	else:
		return None
	return fname


def read(gno, cno, schema_type):
	schemafilename = filename(gno, cno, schema_type)
	if not schemafilename:
		return None
	try:
		f = open(schemafilename)
	except:
		return None
	schema = json.loads(f.read())
	f.close()
	return schema


def write(gno, cno, schema_type, schema):
	schemafilename = filename(gno, cno, schema_type)
	if not schemafilename:
		return
	f = open(schemafilename, 'w+')
	json.dump(schema, f)
	f.close()


def dump(gno, cno, schema_type):
	schema = read(gno, cno, schema_type)
	if schema_type == 'vertex' or schema_type == 'v':
		print('sv: ', end='')
	elif schema_type == 'edge' or schema_type == 'e':
		print('se: ', end='')
	if schema:
		print('[', end='')
		n = len(schema)
		for i, (k,v) in enumerate(schema):
			print(k + ':' + v, end='')
			if i < n - 1:
				print(',', end='')
		print(']')
	else:
		print('None')


def new():
	return []


def check_base_type(base_type):
	base_type_lower = base_type.lower()
	if base_type_lower == 'int' or \
	   base_type_lower == 'float' or \
	   base_type_lower == 'double' or \
	   base_type_lower == 'char' or \
	   base_type_lower == 'string' or \
	   base_type_lower == 'date' or \
	   base_type_lower == 'time':
		return True
	return False


def add(schema, base_type, name):
	if not check_base_type(base_type):
		print('Illegal base type')
		return schema

	if not schema:
		schema = []
	schema.append((base_type.lower(),name))
	return schema
