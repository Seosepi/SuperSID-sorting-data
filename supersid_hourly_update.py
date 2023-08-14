# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 10:55:50 2023

@author: Administrator
"""
import os
import pandas as pd
from datetime import datetime
from config import *

#stations = ["ICV","DHO38","VTX4","FTA","JXN"]
#frequencies = ["20270","23400","19200","20900","16400"]


todays_date = datetime.now ()
dt_string = todays_date.strftime("%d/%m/%Y %H:%M:%S")

today = todays_date.date ()
path = rawfolder

print("Updating SuperSID data to", path, "at "+dt_string)

for filename in os.listdir (path) :
    
        file_time = os.path.getmtime (path + filename)
        file_date = datetime.fromtimestamp (file_time)
        file_day = file_date.date ()
        
        if file_day == today and filename.startswith("hourly") and filename.endswith(str(today)+".csv"):
            print (f'File to copy is {path + filename}.')
            

            # Read header and then 6 data columns (time and amplitude)
            dfheader = pd.read_csv(path + filename, nrows=15,
                                    skipinitialspace=True,
                                    delimiter=',\n',
                                    names=['datetime'])
            print(dfheader)
            dfdata = pd.read_csv(path + filename, skiprows=15,
                         skipinitialspace=True,
                         delimiter=',',
                         names=['datetime', 'Amp_'+stations[0], 'Amp_'+stations[1], 'Amp_'+stations[2], 'Amp_'+stations[3], 'Amp_'+stations[4]])
            print('success')             
            # Write a data file for each station, with updated headers.
            
            for i in range(len(stations)):
                dfheader.iloc[13] = "# StationID = "+str(stations[i])
                dfheader.iloc[14] = "# Frequency = "+str(frequencies[i])
                dfcombined = pd.concat([dfheader,dfdata], ignore_index=True, join="outer")
                filename = path + "Birr_"+stations[i]+"_"+str(today)+".csv"
                dfcombined.to_csv(filename,chunksize=1000,columns=["datetime", "Amp_"+stations[i]], header = None)
                print (f'Writing hourly station file: {filename}')
            
        else:
            print('pass')
            pass