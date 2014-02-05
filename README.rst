Spoutnik-I
==========

Script to retrieve selected satellite metered data from a netcdf file 


netCDF4 installation:
=====================


python-netcdf:
--------------
First looking for the tools included in ubuntu 12.04:

    ~/Spoutnik-I $ apt-cache search netcdf
    
    ~/Spoutnik-I $ sudo apt-get install python-netcdf ncview

    ~/Spoutnik-I $ apt-cache showpkg python-netcdf

The python package "python-netcdf" from the distribution isn't the one imported in the demo with "import netCDF4".
We don't really know how to use it. 

Anyway, every google search about working with python and netcdf sends us to using "import netCDF4" 

netCDF4:
--------
Lots of information about netCDF4 can be accessed from [netCDF4-PiPy].

Usefull documentation about the netcdf format can be found at the demo page [netCDF4-demo]
It seems it's included in a python scientific suite [Anaconda] that may be easily installed.
More easily on Centos/Fedora. But can probably be installed on a Ubuntu [Anaconda-fr].

Anyway we would have to upgrade the netCDF4 package, since it is said in [netCDF4-module] that the Anaconda version [Anaconda], 1.06, has a bug that is fixed in 1.07 to be compatible with ubuntu 12.04.

We'll then first try to install only the last version of netCDF4 (1.0.7), and if it doesn't work we may need a Scientific Linux Station, not to get into too much troubles.

Traditionnal install:
---------------------

The requirements are described in [netCDF4-demo].

    $ sudo apt-get install cython

The HDF5 C library version 1.8.4-patch1 is already present in libhdf5-serial.

    /netCDF4-1.0.7 $ sudo python setup.py install


Install problem 1:
------------------

First the problem with HDF5, needed the "-dev" package:

    genevieve@genevieve-Studio-1535 ~/Téléchargements/netCDF4-1.0.7 $ python setup.py install

    HDF5_DIR environment variable not set, checking some standard locations ..

    checking /home/genevieve ...

    checking /usr/local ...

    checking /sw ...

    checking /opt ...

    checking /opt/local ...

    checking /usr ...

    Traceback (most recent call last):

      File "setup.py", line 205, in <module>

        raise ValueError('did not find HDF5 headers')

    ValueError: did not find HDF5 headers
    
We first tryied to include the corresponding python package, it's useless.

    ~/Spoutnik-I $ apt-cache showpkg python-h5py

    ~/Spoutnik-I $ apt-get install python-h5py
    
In fact the problem already appeared elsewhere [netCDF4 install issue].
In our case there are simply no header files since these are included in the "-dev" package. 
We only needed the "libhdf5-serial-dev" package.

Install problem 2: libnetcdf-dev
--------------------------------

    NETCDF4_DIR environment variable not set, checking standard locations.. 

Install problem 3: python-dev
-----------------------------
    netCDF4.c:16:20: fatal error: Python.h: No such file or directory
    compilation terminated.
    error: command 'gcc' failed with exit status 1

Checking the install:
---------------------
    /netCDF4-1.0.7 $ cd test ; python run_all.py 

It sends us only one warning.

    >>> from netCDF4 import Dataset # Now works!

netCDF4 tutorials:
==================
[netCDF4-demo] and [Stack_ex_1] shows us examples on how to use the module.

References:
===========

[netCDF4-module] https://code.google.com/p/netcdf4-python/

[netCDF4-demo] http://netcdf4-python.googlecode.com/svn/trunk/docs/netCDF4-module.html

[netCDF4-PiPy] https://pypi.python.org/pypi/netCDF4/1.0.7

               https://pypi.python.org/pypi/netCDF4/0.8.2

[Stack_ex_1] https://stackoverflow.com/questions/16641437/importing-variables-from-netcdf-into-python

[Anaconda] http://docs.continuum.io/anaconda/pkgs.html

[Anaconda-fr] http://python-prepa.github.io/preparation.html

[netCDF4 install issue] https://code.google.com/p/netcdf4-python/issues/detail?id=63
