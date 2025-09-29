#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Aaron Siegle (aaron.siegle@duke.edu)
# Date:   Fall 2025
#--------------------------------------------------------------

# Parse Data
# Copy and paste a line of data as the lineString variable value
lineString = "20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0"
  
# Use the split command to parse the items in lineString into a list object
lineData = lineString
  
# Assign variables to specfic items in the list
record_id = lineData[]   # ARGOS tracking record ID
obs_date = lineData[]   # Observation date
ob_lc = lineData[]       # Observation Location Class
obs_lat = lineData[]     # Observation Latitude
obs_lon = lineData[]     # Observation Longitude
  
# Print information to the use
print (f"Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}")

#Create a variable pointing to the data file
# placing an r in front of a file path allows you have the slashes the same way as they are in file explorer
file_name = './data/raw/Sara.txt'

#Create a file object from the file
file_object = open(file_name,'r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

#Pretend we read one line of data from the file
lineString = line_list[200]

#Split the string into a list of data items
lineData = lineString.split()

#Extract items in list into variables
record_id = lineData[0]
obs_date = lineData[2]
obs_lc = lineData[4]
obs_lat = lineData[6]
obs_lon = lineData[7]

#Print the location of sara
print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")