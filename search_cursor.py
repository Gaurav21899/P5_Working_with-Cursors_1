""""
use search cursor to get all the major attractions established after the year 2008

Print the muse and the estab in proper forest.

"""""

import arcpy
import os

gdb_path = r"D:\Programming for GIS-3\P5_Working_with-Cursors_1\ProProject_Cursors\ProProject_Cursors.gdb"
fc_name = "MajorAttractions"
fc_path = os.path.join(gdb_path, fc_name)

# Creating a list of fields to be used in search cursor
fields_list = ["Name", "ESTAB"]

with arcpy.da.SearchCursor(fc_path, fields_list) as s_cursor:
    for row in s_cursor:
        if row[1] >= 1976:
            print("MajorAttraction Name{}, ESTABLISHED {}".format(row[0], row[1]))

print("Process Completed")

