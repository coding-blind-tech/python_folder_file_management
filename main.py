import os
import shutil

directory_name = "my_directory"

if not os.path.exists(directory_name):
    os.mkdir(directory_name)

# Delete empty directory
if os.path.exists(directory_name):
    # os.rmdir(directory_name)
    shutil.rmtree(directory_name)

