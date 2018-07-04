pygrdb User's Guide
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

grdb associates data with the various vertices and edges.  The types of
these data are described by schemas.  Before we describe grdb's schema
model, consider a general graph can have arbitrary schemas for any vertex
and any edge.  This model allows for any arbitrary data to be attached to
any arbitrary graph structure.

![alt text](images/General\ Graph.png "General Graph")
