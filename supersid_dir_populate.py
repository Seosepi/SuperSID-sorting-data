#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 11:03:39 2023

@author: dunsink
"""

# Import Oscar's archiving package (available from github.com/TCDSolar/SIDpy)
import sidpy.run as sid

import pandas as pd
import requests
from pathlib import Path

from datetime import datetime
from config import *

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

#Create CSVs and PNGs and copy to archive. Will then be transferred to vlf.ap.dias.ie at 5 mins past top of each hour.
sid.process_directory([rawfolder], sortedfolder)
print("Copying SuperSID data to", sortedfolder ,"at "+dt_string+" UTC")
