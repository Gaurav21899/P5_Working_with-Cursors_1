"""""

Three different types of cursors:

1.SearchCursor - Reading the attribute data
2.UpdateCursor - Updating the attribute data
3.InsertCursor - Creating new row in the attribute data

"""""

import arcpy
import os

gdb_path = r"D:\Programming for GIS-3\P5_Working_with-Cursors_1\ProProject_Cursors\ProProject_Cursors.gdb"
fc_name = "MajorAttractions"
fc_path = os.path.join(gdb_path, fc_name)

# Creating a list of fields to be used in search cursor
fields_list = ["NAME", "ESTAB"]

# # use a search cursor to establish a read-only access to the feature class
# s_cursor = arcpy.da.SearchCursor(fc_path, fields_list)
#
# # looping through the cursor object
#
# for row in s_cursor:
#     print("{}, {}".format(row[0], row[1]))
#     # print(row[0], row[1])

# Deleting the cursor object

# del s_cursor

with arcpy.da.SearchCursor(fc_path, fields_list) as s_cursor:
    for row in s_cursor:
        print("MajorAttraction Name{}, ESTABLISHED {}".format(row[0], row[1]))

print("Process Completed")
