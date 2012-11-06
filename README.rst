PackBits encoder/decoder
========================

This module implements a PackBits encoder/decoder for Python 2.x and 3.x.

PackBits encoding is used in PSD and TIFF files.

Installation
------------

::

    pip install packbits

Usage
-----

Import ``packbits`` module; then use ``packbits.encode(data)`` and
``packbits.decode(data)`` functions.

Contributing
------------

Development happens at github and bitbucket:

* https://github.com/kmike/packbits
* https://bitbucket.org/kmike/packbits

The main issue tracker is at github: https://github.com/kmike/packbits/issues

Feel free to submit ideas, bugs, pull requests (git or hg) or regular patches.

In order to run tests, install `tox <http://tox.testrun.org>`_ and type

::

    tox

from the source checkout.

The license is MIT.
