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
	base_type_upper = base_type.upper()
	if base_type_upper == 'INT' or \
	   base_type_upper == 'FLOAT' or \
	   base_type_upper == 'DOUBLE' or \
	   base_type_upper == 'CHAR' or \
	   base_type_upper == 'STRING' or \
	   base_type_upper == 'DATE' or \
	   base_type_upper == 'TIME':
		return True
	return False


def size(schema):
	size = 0
	for attrtype, attrname in schema:
		if attrtype == 'INT':
			size += 8
		elif attrtype == 'FLOAT':
			size += 4
		elif attrtype == 'DOUBLE':
			size += 8
		elif attrtype == 'CHAR':
			size += 1
		elif attrtype == 'STRING':
			size += 256
		elif attrtype == 'DATE':
			size += 10
		elif attrtype == 'TIME':
			size += 8
		
	return size


def add(schema, base_type, name):
	if not check_base_type(base_type):
		print('Illegal base type')
		return schema

	if not schema:
		schema = []
	schema.append((base_type.upper(),name))
	return schema
