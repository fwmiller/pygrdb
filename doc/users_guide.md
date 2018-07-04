grdb User's Guide
===================

(C) Frank W. Miller

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
