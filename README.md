# SuperSID-sorting-data
This repo contains 2 scripts. 
supersid_hourly_update.py : splits raw SuperSID buffer files into a file for each transmitter every hour. 
supersid_dir_populate.py : this organises the files created by supersid_hourly_update.py and relocates them to an archive folder.

Config:
1. Edit config file, edit list of vlf transmitters to include your chosen ones aswell as the list of corresponding locations. Ensure that every vlf transmitter and its given location are in the same position of their respective list.
2. Change rawfolder to be the folder where the rawdata is located i.e. the data supersid_hourly_update.py output csv's are located
3. Change sortedfolder to be the desired folder location for the processed and archived data to be stored
4. Both scripts can be ran every hour using the crontab command in linux. Ensure supersid_hourly_update.py is run before supersid_dir_populate.py


