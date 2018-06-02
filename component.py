import os
import re
from config import GRDB_DIR
from vertex import *

def component_get_dir(gno, cno):
	rdir = os.path.expanduser(GRDB_DIR)
	gdir = rdir + '/' + str(gno)
	cdir = gdir + '/' + str(cno)
	return cdir

def components_get_list(gno):
	clist = []
	rdir = os.path.expanduser(GRDB_DIR)
	cdirs = os.listdir(rdir + '/' + str(gno))
	for cdir in cdirs:
		clist.append(cdir)
	return clist

def components_print(gno):
	if gno < 0:
		return
	clist = components_get_list(gno)
	for c in sorted(clist):
		print(str(gno) + '.' + c)

def component_new(gno):
	# Find highest existing component number for specified graph and
	# add one
	clist = components_get_list(gno)
	cnolist = list(map(int, clist))
	cno = max(cnolist or (-1)) + 1

	# Create directory for new component
	cdir = component_get_dir(gno, cno)
	os.mkdir(cdir)

	# Create first vertex in the new component
	vertex_new(cdir)
