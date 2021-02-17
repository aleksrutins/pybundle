========
PyBundle
========
PyBundle is a tool to manage Python projects.

Installation
============

To install, run:

.. code-block:: bash

    python3 -m pip install -r requirements.txt
    sudo python3 setup.py install

(removing ``sudo`` for Windows)

And you will have the ``pyb`` executable installed.

Notes
=====
- In order to use :code:`pyb run`, you must have the ``python3`` executable in your PATH.

Usage
=====
Creating a project
------------------
To create a project, run ``pyb init`` and answer the questions. It will scaffold a basic empty Python project, which can then be run with ``pyb run``.

Adding a dependency
-------------------
To add a dependency, run ``pyb add <package-name>``.
To install all dependencies, use ``pyb install``.