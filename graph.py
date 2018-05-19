import os
from config import GRDB_DIR

def graph_command(argv):
	graphs_print()

def graphs_print():
	rdir = os.path.expanduser(GRDB_DIR)
	dirs = os.listdir(rdir)
	glist = []
	for dir in dirs:
		glist.extend(dir)
	for g in sorted(glist):
		print(g)

def graph_new():
	return
