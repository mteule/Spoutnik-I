#!/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2014 Mathias Teulé <mathias.te@googlemail.com>

# Usefull documentation to create excell files can be found at the
# official homepage:
# http://xlsxwriter.readthedocs.org/tutorial01.html
# sudo pip install XlsxWriter

import xlsxwriter
import spoutnik

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('output_01.xlsx')

sp = spoutnik.Spoutnik()
sp.refresh_indexes()
sp.refresh_var_values()
sp.print_attr()

worksheet_name = sp.ncfile_url + 'date'  # filename <= 31 char

worksheet = workbook.add_worksheet('worksheet_name')

