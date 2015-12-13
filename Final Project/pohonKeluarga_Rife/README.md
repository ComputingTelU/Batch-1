DOCUMENTATION
==================================================

Title : Family Tree :tree:
Group Member :
 - Rizkiyana Prima Putra (R) :coffee:
 - Isa Setiawan (I) :pizza:
 - Fadhil Mulia Abdillah (F) :sparkling_heart:
 - Enki Probo Sidhi (E) :dancer:
 
Introduction
------------------------------------------

This final project implement the tree data structure in a Family Tree way. The main purpose of this algorithm is to know the relationship between two people in the family tree; e.g. people 1 'is parent of' people 2.
For your information, we run our algorithm in python. Thanks

Limitation
------------------------------------------

In this project, searching the relationship between two people is limited to seven type of relationship; i.e. grandparent, parent, child, uncle, nephew, brother, and grandchild.

The Data Structure
------------------------------------------

The main data structure of this project is tree data structure as an object in python. we also add another data structure, Queue, that used in 'searchFamily' method. 
List of property in tree data structure (we named it as Family_Tree object) :
  - name - string - The primary key of the Family_Tree object
  - depth - integer - The depth of a node in a tree, default to 0
  - partner - Family_Tree object - Pointing another Family_Tree object, default to 'None' value
  - children - list of Family_Tree object - list of children

'searchFamily' Method (traversing algorithm)
--------------------------------------------

We use breadth-first search(BFS) as our searching/traversing through tree algorithm that implemented in searchFamily method. Furthermore, you can read about BFS in this link --> [about BFS](https://en.wikipedia.org/wiki/Breadth-first_search).

How To Use
--------------------------------------------

In our example (inside tugasakhirRIFE.py file), First, we create a Family_Tree object that initialized with name 'joko'.
