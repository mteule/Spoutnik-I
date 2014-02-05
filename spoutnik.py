import netCDF4
from netCDF4 import Dataset

# Load the file:
ncfile = Dataset('../Spoutnik-I files/PREVIMER_WW3-FINIS-200M_20140123T13Z.nc','r')

#### Exploring the file's attributes ####
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


