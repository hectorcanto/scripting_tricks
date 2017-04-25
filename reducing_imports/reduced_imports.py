"""
Goal
----
The goal of this example is to show how to filter the imports from one module to another. The straightforward way is to
 list every import, but this works when imports keep growing. A second approach is to use __init__.py to import only
 some of each module of a package.

However the approach here is to filter the imports from the importer side.

Originally, it was meant for a Django app, but can be used out of this case easily

Example
-------

In this example we want to import all AWS related configuration values from a module called settings (the typical
settings.py on a Django app).

We will filter all the variables started by "AWS_". In another file we will import this "middleware" and only import
the AWS variables, and leave out all the auxiliary variables (settings, aws_imports, elemnt)
This scripts is meant for a Djano app, but can be extended to any other filtered import.

The trick resides on making internal or private - adding "_" or "__" respectively - to every auxiliary variable, so the
import mechanisms will left them out.
"""

from app import settings as __settings

__aws_imports = [ _ for _ in dir(__settings) if _.startswith("AWS_") ]


for __element in __aws_imports:
    vars()[__element] = getattr(__settings, __element)
