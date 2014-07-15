#!/usr/bin/env python

#Author: Dale Housler
#NavigateLigandDirs.py
#11-06-2014

#This program navigates between the ligand directories to add to the automation
#if there are one or more ligand directories.

import os #Allows for operating system commands
import re

#Start in the PDB folder
start_directory = os.getcwd()
notFile = ("pdb", "mol2", "csv", "txt", "py","kin","log","rsa") # this is the NOT set only want directories NOT files remove by file type .XXX

#Get the ligand directories
directories = [f for f in os.listdir(start_directory) if not f.endswith(notFile)]
print(directories)
#sortedDirectories = directories.sort()
#print(sortedDirectories)
dirLength = len(directories)

i=1

for i in range(0,dirLength):
    os.chdir(directories[i])
    print("\n ----- YOU ARE IN THE " + directories[i] + " DIRECTORY-----\n")
    
    os.system('ls')

    os.system('python3.3 /root/proCLic_package/pro_CLic_MENU.py')

    os.chdir("..")


