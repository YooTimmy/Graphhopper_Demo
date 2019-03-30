##Python version: 3.6.6
##Packages Used: requests, tkinter, itertools, webbrowser, json, utility

##How to use:
In the command line, cd to the folder level of GUI.py, type in "python GUI.py"

##Input file:
location_data.txt -> store the coordinates data for interested locations.
Example:
Longitue,Latitude
1.346005319,103.7553591
1.330751766,103.9356002
1.378135921,103.838826

##GUI instruction:
Enter the input file name into text box (e.g. location_data.txt)
1) Check_Input: It will show how many data points inside the file and return the list.
2) Show_Map: It will open in browser what are the routing plan betweeb each pair of points.
3) Download_Route: It will download the routing information in json format and store in the output.txt file.
4) Upload_Route: It will extract the needed data from output.txt file and show the routing information again inside brower.
5) Display_Route: It will summarize the rouing information and display in the UI.