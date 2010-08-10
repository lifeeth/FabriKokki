.. FabriKokki -- Fabric + Kokki = Awesome documentation master file, created by
   sphinx-quickstart on Mon Aug  9 12:33:26 2010.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to FabriKokki -- Fabric + Kokki = Awesome's documentation!
==================================================================

==========
FabriKokki
==========

.. include:: ../README

Installation
============

There are no stable releases yet. The only sane way to get FabriKokki is to
pull the github repository and:

    python setup.py develop

Stable releases will be able to be installed using::

    easy_install fabrikokki

or::

    pip install fabrikokki

Extra cookbooks can be found at: http://github.com/samuel/kokki-cookbooks

Parent Projects
===============

You can find the latest Kokki version at http://github.com/samuel/kokki

The latest Fabric can be found at http://github.com/bitprophet/fabric

Overview
========

To use FabriKokki, we recommend the following project layout::

    /your_project
        config.yaml
        fabfile.py
        /recipes
            /recipe1
                /recipes
                /templates

Our demo project follows this layout exactly.

To actually run FabriKokki, you are actually leveraging the Fabric command to
pull in specially written replacements for portions of Kokki that
transparently convert local recipes to work remotely without having to
install/copy everything in Kokki to the server which is its normal mode of
action.


Operation
=========

.. todo:: finish this section

    A FabriKokki setup is driven by two main files, the fabfile.py and
    config.yaml.

    A special import...brings in all the required support code from FabriKokki.
.. todo:: document the special import

    The command line is just like Fabric's normal one ::

        fab [-c config_file] -r role -H host -u user -p password

    Order of operation is::

        Initialize Kokki with the file config_file if provided, otherwise use
        config.yaml.

        Read the config.yaml -- this is Kokki's config file as documented in
        Kokki's documentation

        Read directories in `cookbook_paths:` item in config_file.yaml

        For dir in `cookbook_paths`:
            import package, run __init__.py as usual

Example
=======

These are the source files for the example project.

config.yaml::

.. code-block:: yaml
.. include:: ../fabrikokki_demo/config.yaml

.. code-block:: python
.. include:: ../fabrikokki_demo/fabfile.py

To run the 'web' role on the local system::

    fab -c config.yaml -r web

TOC
===

.. toctree::
   :maxdepth: 2

   resources


TOC
===

.. toctree::
   :maxdepth: 2

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

