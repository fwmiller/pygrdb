import config
import os


def get_list(gno):
	clist = []
	rdir = os.path.expanduser(config.GRDB_DIR)
	cdirs = os.listdir(rdir + '/' + str(gno))
	for cdir in cdirs:
		clist.append(cdir)
	return clist
