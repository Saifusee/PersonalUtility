# Program to modify subtitles name of udemy to match with video name by removing certain common keyword
# Valid to Home directory and inside sub directory to one level
import os
import shutil

# Creating list of all files in home directory with .srt extension
files = [data for data in os.listdir() if data.endswith(".srt")]
# Creating list of all directories present
sub_dir = [data for data in os.listdir() if os.path.isdir(data)]

sub_files = list()
# Adding name of files of subdirectories to main file list
for element in  sub_dir:
    if os.path.isdir(element):
        sub = [os.path.join(element,data) for data in os.listdir(element) if data.endswith(".srt")]
        sub_files = sub_files + sub
files = files + sub_files
# Creating new list of files name by removing English from all file names
new_files = [data.replace(" English", "") for data in files if __name__ == "__main__"]


length = len(files)
new_path = "..\\abc"
# Performing desired operation
for i in range(length):

    # # When renaming srt files
    # os.rename(files[i], new_files[i])

    # # When creating copy to of all srt files to new location
    # # Getting name of each file with directory
    # path_to_file = os.path.join(new_path, files[i])
    # # finding index of last blacklash to remove file name from last directory
    # last_backslash_index = path_to_file.rfind("\\")
    # directory_name = path_to_file[0:last_backslash_index]
    # # Creating directory first if already exists then move on
    # os.makedirs(directory_name, exist_ok=True)
    # shutil.copy(files[i], os.path.join(new_path, files[i]))

    pass