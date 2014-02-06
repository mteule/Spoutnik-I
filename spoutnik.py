


import netCDF4
from netCDF4 import Dataset

# Load the file:
ncfile = Dataset('../Spoutnik-I files/PREVIMER_WW3-FINIS-200M_20140123T13Z.nc','r')

####### Exploring the file's attributes #######
ncfile.netcdf_version
ncfile.format_version

# First look at it:
ncfile.variables
ncfile.dimensions
ncfile.dimensions.keys()

# Dimensions:
print (ncfile.variables[u'time'])
print (ncfile.variables[u'latitude'])
print (ncfile.variables[u'longitude'])

# Variables:
var_list = list(['hs','hs0','hs1','dir','th0','th1','tp0','tp1','tp2'])

for var in var_list:
    print (ncfile.variables[var])


print (ncfile.variables[u'longitude'].shape)
print (ncfile.variables[u'longitude'][:])
print (ncfile.variables[u'time'][:])

    #################################################
    # netCDF File Exploration with Python and NumPy #
    #################################################

# http://nbviewer.ipython.org/github/Unidata/tds-python-workshop/blob/master/reading_netCDF.ipynb
# [L'explication]

# Led by this tutorials it is quite easy to obtain the value of a variable for one point.


#=====> "Let's find out more about temperature and salinity"
#-----------------------------------------------------------

####### Get the variable objects #######

# doesn't read any data yet, just metadata read in when netCDF dataset opened
# notice these two variables are the same shape, defined on the same 4D grid

hs = ncfile.variables[u'hs']
hs0 = ncfile.variables[u'hs0']
hs1 = ncfile.variables[u'hs1']
dir = ncfile.variables[u'dir']
th0 = ncfile.variables[u'th0']
th1 = ncfile.variables[u'th1']
tp0 = ncfile.variables[u'tp0']
tp1 = ncfile.variables[u'tp1']
tp2 = ncfile.variables[u'tp2']

print hs
print hs0
print hs1
print dir
print th0
print th1
print tp0
print tp1
print tp2

#=====> "List the attributes of temperature"
#-------------------------------------------

####### List the attributes of dir #######
# We can get
# a list of the names of netCDF attributes for a variable using the ncattrs() method
# the value of an attribute using Python's var.att syntax
for att in dir.ncattrs():
    print att



print dir.coordinates  # raise AttributeError: NetCDF: Attribute not found
print dir.standard_name
print dir.units


####### What is the sea surface temperature and salinity at 50N, 140W? #######
#-----------------------------------------------------------------------------

# From this part of the tutorial, 
# we have to behave differently since we do not have the "coordinates" variable.
for d in dir.dimensions:
    print(d),

####### NumPy #######
#--------------------

# To access netCDF data, rather than just metadata, we will also need NumPy.

import numpy as np # in fact it seems we won't have to use it. 

# Variables:
print hs
print hs0
print hs1
print dir

# =====> Finding the latitude and longitude indices of 50N, 140W
#---------------------------------------------------------------

# Dimensions:
    ####### Get the dimension objects #######
time = ncfile.variables[u'time']
latitude = ncfile.variables[u'latitude']
longitude = ncfile.variables[u'longitude']

print time
print latitude
print longitude

#### Here we can see that the dimensions have a "axis" attribute:
# X for longitude
# Y for latitude

#### There is some difference between his case and ours:
# His case:
# float32 Latitude(u'Y', u'X')
# float32 Longitude(u'Y', u'X')

# Our case:
# float32 latitude(latitude)
# float32 longitude(longitude)

#### Our situation may be much easier:

# We can retrieve Dimension values easily
print (ncfile.variables[u'time'][:])
print (ncfile.variables[u'longitude'][:])
print (ncfile.variables[u'latitude'][:])

# Have one point:
print dir
# [blabla...] int16 dir(time, latitude, longitude) [blabla...]

print dir[0, 48.80160141, -4.103333] # raise OverflowError: can't convert negative value to unsigned PY_LONG_LONG
print dir[0, 1, 1]
print dir[0, 640, 500] # raise IndexError
print dir[0, 639, 499], dir.units

print time[0], time.units
# It seems obvious that this things uses indexes...


####### How to get the good time format #######


times = time
jd = netCDF4.num2date(times[:],times.units)
jd
print jd

####### How to get the good indexes #######
type(ncfile.variables[u'latitude'][:])

#############################################################################
# Trying to have the point indexes:

# http://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html
# Not better: http://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html

# [Solution]: http://nbviewer.ipython.org/gist/rsignell-usgs/4740419
# Inspired from the above, but much simpler.
lat_values = (ncfile.variables[u'latitude'][:]).copy()
lat_pt = 48.29793167114258

# First try
dist_sq = (lat_values - lat_pt)**2
index = dist_sq.argmin()
type(index)
index

# To a function:
def index(pt, ndarray):
    ndarray_cp = ndarray.copy()
    dist_sq = (ndarray_cp - pt)**2
    index = dist_sq.argmin()
    return index

##############################################################################
##############################################################################
##############################################################################
##############################################################################
# This part works by itself:

import netCDF4
from netCDF4 import Dataset

# Load the file:
ncfile = Dataset('../Spoutnik-I files/PREVIMER_WW3-FINIS-200M_20140123T13Z.nc','r')

point_indexes = dict({'lat':0,'lon':0})
point = dict({'lat':48.29793167114258,'lon':-4.976805686950684})

point_indexes['lat'] = index(point['lat'], ncfile.variables[u'latitude'][:])
point_indexes['lon'] = index(point['lon'], ncfile.variables[u'longitude'][:])
point_indexes

times = ncfile.variables['time']
jd = netCDF4.num2date(times[:],times.units)

# for that point, retrieve the values for the variable list:
var_list = list(['hs','hs0','hs1','dir','th0','th1','tp0','tp1','tp2'])

print jd

print "point: ", point

for i in var_list:
    var = ncfile.variables[i]
    print i, "(", var.units ,"): ", var[0, point_indexes['lon'], point_indexes['lat']]





