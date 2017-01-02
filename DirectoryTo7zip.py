#------------------------------------------------------------------------------
# This file compresses all files from user entered directory into a 7-zip file
# User Inputs: 1. Enter the full path of the directory to be compressed
#              2. Enter the name of target 7-zip file
# Author: Swapnali Gujar
# Date of Creation: Nov-11-2016
#----------------------------------------------------------------
import os
import sys
import re
import subprocess


#Make 7z files from directories preset at local directory
dir_to_7zip = input("Enter directory to compress in 7zip: ")
zFileName = input("Enter name of target 7zip file: ")
#print("Files to archive from: ", name)
zFileName = zFileName+".7z"
zFile = ' "' + os.path.join(dir_to_7zip, zFileName) + '"  '
print("Target 7-zip file location is: ", zFile)

dir_to_7zip = dir_to_7zip+'\\'
dirbase =os.path.splitdrive(dir_to_7zip)

if os.path.isdir(dir_to_7zip):
    # create temporary listfile
    text_path = dirbase[0] + '\sample.txt'
    outFile = open(text_path, 'w')
    outFile.write(dir_to_7zip+ "\*.*")
    outFile.close()
    text_path_at = " @" + '"' + text_path + '"'
    print("Please wait...")
    subprocess.call(r'"C:\Program Files\7-Zip\7z.exe" ' + " a" + zFile + text_path_at)
    #delete temporary listfile
    os.remove(text_path)
else:
    print("No valid directory found, goodbye")
