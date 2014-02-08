#!/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2014 Mathias Teulé <mathias.te@googlemail.com>

# Usefull documentation to create excell files can be found at the
# official homepage:
# http://xlsxwriter.readthedocs.org/tutorial01.html

import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('output_01.xlsx')
worksheet = workbook.add_worksheet()

