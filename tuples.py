import config
import struct

def dump(s, fd):
	if not s:
		return

	# Iterate through the attributes of the schema and print the values
	# associated with the current tuple
	first = True
	print('[', end='')

	for attrtype, attrname in s:
		if attrtype == 'INT':
			b = fd.read(config.BASE_TYPE_SIZES['INT'])
			if not b:
				break
			if not first:
				print(',', end='')
			first = False
			print(struct.unpack('<q', b)[0], end='')

		elif attrtype == 'UINT':
			b = fd.read(config.BASE_TYPE_SIZES['UINT'])
			if not b:
				break
			if not first:
				print(',', end='')
			first = False
			print(struct.unpack('<Q', b)[0], end='')

		elif attrtype == 'FLOAT':
			b = fd.read(config.BASE_TYPE_SIZES['FLOAT'])
			if not b:
				break
			if not first:
				print(',', end='')
			first = False
			d = struct.unpack('d', b)[0]
			print(d, end='')

		elif attrtype == 'DOUBLE':
			b = fd.read(config.BASE_TYPE_SIZES['DOUBLE'])
			if not b:
				break
			if not first:
				print(',', end='')
			first = False
			d = struct.unpack('d', b)[0]
			print(d, end='')

		elif attrtype == 'CHAR':
			b = fd.read(config.BASE_TYPE_SIZES['CHAR'])
			if not b:
				break
			if not first:
				print(',', end='')
			first = False
			print(str(b), end='')

		elif attrtype == 'STRING':
			b = fd.read(2)
			len = struct.unpack('<H', b)[0]
			if len > 0:
				b = fd.read(config.BASE_TYPE_SIZES['STRING'])
				if not b:
					break
			if not first:
				print(',', end='')
			first = False
			if len == 0:
				print('\'\'', end='')
			else:
				print('\'' + b[:len].decode('utf-8') + '\'', end='')

		elif attrtype == 'DATE':
			b = fd.read(config.BASE_TYPE_SIZES['DATE'])
			if not b:
				break
			if not first:
				print(',', end='')
			first = False
			s = str(b)
			print(s, end='')

		elif attrtype == 'TIME':
			b = fd.read(config.BASE_TYPE_SIZES['TIME'])
			if not b:
				break
			if not first:
				print(',', end='')
			first = False
			s = str(b)
			print(s, end='')

	print(']', end='')
