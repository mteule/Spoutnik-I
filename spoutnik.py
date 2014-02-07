#!/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2014 Mathias Teulé <mathias.te@googlemail.com>


import netCDF4
from netCDF4 import Dataset

# Load the file:
ncfile = Dataset('../Spoutnik-I files/PREVIMER_WW3-FINIS-200M_20140123T13Z.nc','r')

point_indexes = dict({'lat':0,'lon':0})
point = dict({'lat':48.29793167114258,'lon':-4.976805686950684})

def index(pt, ndarray):
    ndarray_cp = ndarray.copy()
    dist_sq = (ndarray_cp - pt)**2
    index = dist_sq.argmin()
    return index

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


