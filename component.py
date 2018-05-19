import os
from config import GRDB_DIR

def components_print():
	rdir = os.path.expanduser(GRDB_DIR)
	gdirs = os.listdir(rdir)
	for gdir in gdirs:
		print('Graph', gdir)
		cdirs = os.listdir(rdir + '/' + gdir)
		for cdir in cdirs:
			print(cdir)
