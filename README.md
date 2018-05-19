pygrdb - grdb in Python 3
=========================

pygrdb is an open-source graph database being developed at the University of
Colorado.  pygrdb is written in Python 3.

Contact
-------

frank.miller@colorado.edu


Database File System Layout
---------------------------

The database is kept in the user's home directory in a directory called
.grdb.

This directory contains one directory for each graph maintained in the
database.

Each graph directory contains on directory for each component of that graph.

Each component directory contains the following files:
1. Vertex schema
2. Edge schema
3. Vertex file
4. Edge list file

The two schema files are maintained as JSON formatted text files.

The edge list file contains a flag in the JSON indicating whether the
edges are directed or undirected.

The vertex file is maintained as a binary file containing a vertex id and
associated tuple data for each vertex.

The edge list file is maintained as a binary file containing the two vertex
id's of the vertices the edge connects and associated tuple data for each
edge.
