import component
import os
import schema


def update_vertex_tuples(gno, cno, old_schema_size):
	sv = schema.read(gno, cno, 'v')
	schema_size = schema.size(sv)

	vfile = component.get_dir(gno, cno) + '/v'
	fd1 = open(vfile, 'rb')
	fd2 = open(vfile + '.tmp', 'wb+')

	while True:
		vb = fd1.read(8)
		if not vb:
			break;

		vtuple = fd1.read(old_schema_size)
		if not vtuple:
			break;

		fd2.write(vb)
		fd2.write(vtuple)
		b = (0).to_bytes(schema_size - old_schema_size)
		fd2.write(b)

	fd2.close()
	fd1.close()

	os.rename(vfile, vfile + '.bak')
	os.rename(vfile + '.tmp', vfile

	# XXX Remove old vertex file backup


def update_edge_tuples(gno, cno, old_schema_size):
	return
