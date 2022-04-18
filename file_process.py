import os, math, glob, re
from glob import glob
import shutil
local_directory = "manifest-1648614027572\LIDC-IDRI"
new_data_directory = "LIDC-IDRI"

for scan_id in os.listdir(local_directory):
    scan_path = os.path.join(local_directory, scan_id)
    new_scan_path = os.path.join(new_data_directory, scan_id)
    if os.path.isdir(scan_path):
        count = 0
        for x in os.walk(scan_path):
            files = [y for y in glob(os.path.join(x[0], '*.dcm'))]
            if len(files) > 0:
                count += 1
                if count > 1:
                    new_scan_path += "-" + str(count)
                shutil.copytree(x[0], new_scan_path)