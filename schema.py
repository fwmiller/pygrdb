import json
import os
from config import *

def schema_read(gno, cno, schema_type):
	# Check whether a schema exists
	cdir = os.path.expanduser(GRDB_DIR) + '/' + str(gno) + '/' + str(cno)
	if schema_type == 'vertex':
		schemafilename = cdir + '/' + VERTEX_SCHEMA_FILE

	elif schema_type == 'edge':
		schemafilename = cdir + '/' + EDGE_SCHEMA_FILE

	else:
		return None

	# Read in the JSON schema to a dictionary version
	try:
		schemafile = open(schemafilename)
	except:
		return None

	schemastr = schemafile.read()
	schema = json.loads(schemastr)

	return schema

def schema_write(schema, gno, cno):
	return

def schema_print(gno, cno, schema_type):
	schema = schema_read(gno, cno, schema_type)

def schema_new():
	return {}

def schema_add(schema, name, base_type):
	if not schema:
		schema = {}
	schema[name] = base_type
	return schema
