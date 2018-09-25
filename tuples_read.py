import config
import struct

def read_attribute(attrtype, fd):
	if attrtype == 'INT':
		b = fd.read(config.BASE_TYPE_SIZES['INT'])
	elif attrtype == 'UINT':
		b = fd.read(config.BASE_TYPE_SIZES['UINT'])
	elif attrtype == 'FLOAT':
		b = fd.read(config.BASE_TYPE_SIZES['FLOAT'])
	elif attrtype == 'DOUBLE':
		b = fd.read(config.BASE_TYPE_SIZES['DOUBLE'])
	elif attrtype == 'CHAR':
		b = fd.read(config.BASE_TYPE_SIZES['CHAR'])
	elif attrtype == 'STRING':
		b = fd.read(2)
		len = struct.unpack('<H', b)[0]
		if len > 0:
			b = fd.read(config.BASE_TYPE_SIZES['STRING'])

	elif attrtype == 'DATE':
		b = fd.read(config.BASE_TYPE_SIZES['DATE'])
	elif attrtype == 'TIME':
		b = fd.read(config.BASE_TYPE_SIZES['TIME'])


def read(s, fd):
	if not s:
		return

	# Iterate through the attributes of the schema and just read
	# the tuple data
	for attrtype, attrname in s:
		read_attribute(attrtype, fd)
