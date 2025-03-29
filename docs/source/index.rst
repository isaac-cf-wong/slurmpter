.. slurmpter documentation master file, created by
   sphinx-quickstart on Tue Oct 27 13:38:47 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root ``toctree`` directive.

Slurmpter Home
==============

.. image:: https://gitlab.com/isaac-cfwong/slurmpter/badges/master/pipeline.svg
    :target: https://gitlab.com/isaac-cfwong/slurmpter/commits/master

.. image:: https://gitlab.com/isaac-cfwong/slurmpter/badges/master/coverage.svg
    :target: https://codecov.io/gl/isaac-cfwong/slurmpter/

.. image:: https://badge.fury.io/py/slurmpter.svg
    :target: https://pypi.org/project/slurmpter/
    :alt: Package on PyPI

.. image:: https://anaconda.org/conda-forge/slurmpter/badges/version.svg
    :target: https://anaconda.org/conda-forge/slurmpter

.. image:: https://readthedocs.org/projects/sphinx/badge/?version=master
    :target: https://slurmpter.readthedocs.io/en/latest/

.. image:: https://img.shields.io/badge/License-MIT-blue.svg
    :target: https://gitlab.com/isaac-cfwong/slurmpter/-/blob/master/LICENSE

Slurmpter (Slurm Scripter) is a package to build Slurm submit files of a workflow of jobs easily. The package uses PyCondor_ as the backend. The user interface of slurmpter is very similar to that of PyCondor_ except for some arguments dedicated for Slurm.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. _PyCondor: https://github.com/jrbourbeau/pycondor

.. toctree::
    :maxdepth: 1
    :caption: Getting Started

    installation
    tutorial

.. toctree::
    :maxdepth: 1
    :caption: User Guide

    api
    slurm
    slurmjob
    example
    alias
    changelog

.. toctree::
    :maxdepth: 1
    :caption: Useful links

    slurmpter @ GitLab <https://gitlab.com/isaac-cfwong/slurmpter>
    slurmpter mirror @ GitHub <https://github.com/isaac-cfwong/slurmpter>
    Issue tracker <https://gitlab.com/isaac-cfwong/slurmpter/-/issues>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
