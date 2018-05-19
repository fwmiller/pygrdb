import os
from config import GRDB_DIR

def graphs_print():
	rootdir = os.path.expanduser(GRDB_DIR)
	dirs = os.listdir(rootdir)
	for dir in dirs:
		print(dir)
