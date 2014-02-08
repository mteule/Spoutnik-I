#!/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2014 Mathias Teulé <mathias.te@googlemail.com>


import netCDF4
from netCDF4 import Dataset


class Spoutnik(object):

    ncfile_url = None
    ncfile = None
    point = dict({'lat': 48.29793167114258, 'lon': -4.976805686950684})
    point_indexes = dict({'lat': 0, 'lon': 0})
    var_list = \
        list(['hs', 'hs0', 'hs1', 'dir', 'th0', 'th1', 'tp0', 'tp1', 'tp2'])
    var_values = list()

    def __init__(self, file_url=
        '../Spoutnik-I files/PREVIMER_WW3-FINIS-200M_20140123T13Z.nc'):

        self.ncfile_url = file_url
        self.__load_ncfile()
        pass

    def __load_ncfile(self):
        """
        Load the netcdf file
        """
        self.ncfile = Dataset(self.file_url, 'r')
        pass

    def __refresh_index(self, pt, ndarray):
        """
        Retrieve from the numpy.ndarray the index of a given value of the array
        """
        ndarray_cp = ndarray.copy()
        dist_sq = (ndarray_cp - pt) ** 2
        index = dist_sq.argmin()
        return index

    def refresh_indexes(self):
        # Latitude
        self.point_indexes['lat'] = self.__refresh_index(
            self.point['lat'], self.ncfile.variables[u'latitude'][:])
        # Longitude
        self.point_indexes['lon'] = self.__refresh_index(
            self.point['lon'], self.ncfile.variables[u'longitude'][:])
        pass

    def refresh_var_values(self):
        del(self.var_values[:])
        for i in self.var_list:
            var_value = dict({'name': "", 'value': 0, 'units': ""})
            var = self.ncfile.variables[i]
            var_value['name'] = i
            var_value['units'] = var.units
            var_value['value'] = \
                var[0, self.point_indexes['lon'], self.point_indexes['lat']]
            self.var_values.append(var_value)
        pass

    def print_attr(self):

        # format the date:
        times = self.ncfile.variables['time']
        jd = netCDF4.num2date(times[:], times.units)

        # print Dimensions:
        print "date: ", jd
        print "point: ", self.point
        print "point_indexes: ", self.point_indexes
        print ""

        # print Variables:
        for i in self.var_values:
            print ("  " +
                i['name'] +
                ":\t" +
                str(i['value']) +
                "\t" +
                i['units']
                )
        pass

    pass

if __name__ == "__main__":
    sp = Spoutnik()
    sp.refresh_indexes()
    sp.refresh_var_values()
    sp.print_attr()


