import json
import os
from config import *

def schema_filename(gno, cno, schema_type):
	fname = os.path.expanduser(GRDB_DIR)
	fname += '/' + str(gno)
	fname += '/' + str(cno)
	if schema_type == 'vertex' or schema_type == 'v':
		fname += '/' + VERTEX_SCHEMA_FILE
	elif schema_type == 'edge' or schema_type == 'e':
		fname += '/' + EDGE_SCHEMA_FILE
	else:
		return None
	return fname

def schema_read(gno, cno, schema_type):
	schemafilename = schema_filename(gno, cno, schema_type)
	if not schemafilename:
		return None
	try:
		f = open(schemafilename)
	except:
		return None

	schema = json.loads(f.read())
	f.close()
	return schema


def schema_write(schema, gno, cno, schema_type):
	schemafilename = schema_filename(gno, cno, schema_type)
	if not schemafilename:
		return

	print('Write schema', schema)

	f = open(schemafilename, 'w+')
	json.dump(schema, f)
	f.close()


def schema_print(gno, cno, schema_type):
	schema = schema_read(gno, cno, schema_type)

	if schema_type == 'vertex' or schema_type == 'v':
		print('sv: ', end='')
	elif schema_type == 'edge' or schema_type == 'e':
		print('se: ', end='')

	print(schema)


def schema_new():
	return {}


def schema_add(schema, name, base_type):
	if not schema:
		schema = {}
	schema[name] = base_type
	return schema
