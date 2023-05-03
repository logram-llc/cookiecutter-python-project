.. python-divvy documentation master file, created by
   sphinx-quickstart on Thu Jul 16 15:59:44 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

{{ cookiecutter.project }} |version|
========================================

{{ cookiecutter.description }}

Version: |version|

Tests
-------------

Run all tests with the following command.

::

    pip install .[testing]
    tox -e type,lint

Reference
---------------

Read the reference for a more detailed look at the package.

.. toctree::
   :maxdepth: 5

   /modules