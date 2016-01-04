# !/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
from sys import argv
import unicodecsv
import datetime as dt
import numpy as np
import pandas as pd
from pandas import DataFrame


# add filename argument to command line in order to streamline csv input process
# execute python script as follows: python UsageReportExport.py filename.csv
filename = sys.argv[1]

# using Pandas for table view to rename '\xef\xbb\xbfId' to 'Id'. The parse_dates variable will automatically parse dates from columns in argument directly into proper format.
df = pd.read_csv(filename, parse_dates=[3,5,7,12,18,24,30,36,42])
df.rename(columns = {'\xef\xbb\xbfId':'ID'}, inplace=True)

# add column between ID and Client Name called "Usage Week Of"
df.insert(1,"Usage Week Of", dt.datetime.today().strftime("%Y-%m-%d"))

# replace all commas with space, asked on stackoverflow for help.
df['Client Name'].astype(str)
df["Client Name"] = df["Client Name"].str.replace(","," ")

# make column: AM “Affiliate Login"
# there are 49 columns in this csv
df.insert(48, "Sum of Usage", 0)
df.insert(49, "Affiliate Portal Login", 0)
df.insert(50, "Admin Portal Login", 0)
df.insert(51, "Buyer Portal Login", 0)
df.insert(52, "Admin API Calls", 0)
df.insert(53, "Other API Calls", 0)

# Create "Sum of Usage" column and sum up usage columns and print results in sum of usage column
# Usage Generated columns are "objects" need to convert to "integers"
df['Sum of Usage'] = df['Clicks Generated'] + df['Leads Generated']

# export this son of a bitch, index = False makes sure that the additional row numbers are not included in the export
df.to_csv('~/testandnoted.csv', index = False)
