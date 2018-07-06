grdb User's Guide
===================

&#169; Frank W. Miller

Introduction
------------

grdb is a graph database engine.  It stores and processes large,
heterogeneous datasets (i.e. datasets that are larger than main memory)
that are modeled using a graph structure.  This differs from traditional
databases where data is typically modeled using tables or more formally,
relations.  The goal is to enable graph algorithms to be executed
efficiently across very large, persistent, heterogeneous graph datasets.

grdb associates data with the various vertexes and edges.  The types of
these data are described by schemas.  Before we describe grdb's schema
model, consider a general graph can have arbitrary schemas for any vertex
and any edge.  This model allows for any arbitrary data to be attached to
any arbitrary graph structure.

![alt text](https://github.com/fwmiller/pygrdb/blob/master/doc/images/general_graph.png "General Graph")

*An arbitrary graph with arbitrary schemas*

In this graph, each vertex has a vertex id that is unique across the graph.
Vertexes and edges can have arbitrary schemas.  For example, vertex 2 has
a schema that consists of two attribute types, A and B.  Likewise, the edge
from vertex 2 to vertex 3 has a schema that consists of two attributes,
C and D.  A,B,C,D represent types.  The attribute A might be an integer
and B might be a date

A general graph, like the one shown here, is stored in grdb as sets of
connected components that share a vertex id space.  Each component has
a common schema for all its vertices and common schema for all its edges.
The basis of decomposition of the general graph for storage into components
is these common schemas across the vertices and edges.

![alt text](https://github.com/fwmiller/pygrdb/blob/master/doc/images/decomposed_graph.png "Decomposed Graph")

*A decomposition into a set of connected components with common schemas*

grdb is persistent.  When you enter or manipulate data in the database,
it is all stored on secondary (i.e. persistent) storage.  All the graphs
managed for a given user are stored in a specific file structure.
The user's database is kept in the user's home directory in a directory
called ~/.grdb

This directory contains one directory for each graph maintained in the
database.  Each graph directory contains on directory for each component
of that graph.

Each component directory contains the following files:
1. Vertex schema
2. Edge schema
3. Vertex file
4. Edge list file

The two schema files are maintained as JSON formatted text files.  The
edge list file contains a flag in the JSON indicating whether the edges
are directed or undirected.  The vertex file is maintained as a binary
file containing a vertex id and associated tuple data for each vertex.
The edge list file is maintained as a binary file containing the two vertex
id's of the vertices the edge connects and associated tuple data for each
edge.

Interactive Use
---------------

When the database starts up you get an interactive command prompt:

``$ ./grdb`` \
``grdb (C) Frank W. Miller`` \
``grdb>``

Most commands have two forms, a long form and an abbreviation.  For example,
the graph command can be issued using either ``graph`` or ``g``.


### Creating a Graph

When you start the database for the first time (or after you issue the
``clear`` command), the database is empty, i.e. it contains no graphs.  To
create a graph issue the following commands:

``grdb> g n`` \
``0.0> g`` \
``0.0: ({1},{})`` \
``0.0> ``

The first command creates a new graph.  ``g`` is the graph command and ``n``
the create new graph operation.  The result is a new graph with a single
component that has a single vertex with the vertex id 1 in it.  If you
just type ``g`` as shown in the second command, the list of all the graphs
in the database is printed.

Notice that the command prompt has now changed from ``grdb`` to ``0.0:``
The new graph was assigned the name ``0.0``.  The first digit indicates
graph number 0 and the second digit indicates compnent number 0 associated
with graph 0.
