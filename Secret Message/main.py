import os
import re

def rename_files():
    saved_path = os.getcwd()
    file_list = os.listdir(r"" + saved_path + "\prank")

    os.chdir(saved_path + "\prank")

    for file_name in file_list:
        os.rename(file_name, re.sub('[0-9]', '', file_name))
    os.chdir(saved_path)

rename_files()
