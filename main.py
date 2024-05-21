"""
    @owner: Coding Blind Tech.
    @Description: Python code showing how to perform different operations using the "os" library. This incompasses the following for now:
        - Create and remove directory(s)
        - Write, read, and delete files

    This repository is guided to be written in a way for beginner level programmers to learn from.
"""

import os
import shutil

# Setup variables for directory and filename
directory_name = "my_directory"
filename = "my_file.txt"

# Make sure directory doesn't already exist
if not os.path.exists(directory_name):
    # Create the directory
    os.mkdir(directory_name)


# Note: Below we use the context manager
# # This is the safe way of opening files to avoid having to manual close the file when done

# Create a reference to the file
filename_location =  os.path.join(directory_name, filename)

# Write to a file
# If it is not created already, then it will be automatically created here
# with open(filename_location, "w") as file:
#     file.write("Hello, World!")

# Read from a file
with open(filename_location, "r") as file:
    file_contents = file.read()
    print(f"This is the file contents: {file_contents}")


# Now removing the file
# Lets make sure it exist before we do
if not os.path.exists(filename_location):
    print("File does not exists, so not removing.")
else:
    os.remove(filename_location)
    print("File has been deleted.")



# Delete empty directory
# if os.path.exists(directory_name):
    # os.rmdir(directory_name)
    # shutil.rmtree(directory_name)

