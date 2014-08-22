#!/usr/bin/env python
#Author: Dale Housler
#OS: UNIX & WINDOWS
# ConformationFolders.py

#This program creates the folders for conformation files
#The user runs this program by selecting misc menu from the proCLic Menu

import os
import re
import shutil

confDirs = []

def moveFINALConf_files(confDirs):

    start_directory = os.getcwd()
    
    pdbFilesOnly =  [f for f in os.listdir(start_directory) if  f.endswith(".pdb")]

    pdbFilesOnly.sort()

    #print(len(pdbFilesOnly))
    
    for i in range(len(pdbFilesOnly)):
        #print(pdbFilesOnly)

        period_split = re.split('\.',pdbFilesOnly[i])
        #print(period_split)
        
        if len(period_split[0]) == 8:
            dirname = list(period_split[0])
            dirname = dirname[-4:]
            dirname = ''.join(dirname)
            if not os.path.exists(dirname):
                os.makedirs(dirname)

            #print(dirname)

            shutil.copy2(pdbFilesOnly[i], dirname)

            confDirs += [dirname]
            #print(confDirs)

    for i in range(len(pdbFilesOnly)):
        if len(pdbFilesOnly[i]) > 13:

            for j in range(len(confDirs)):
                shutil.copy2(pdbFilesOnly[i], confDirs[j])
        
        

###END DEF
                
dirname = moveFINALConf_files(confDirs)

print("Conformation directories created and all relevant files moved.")

