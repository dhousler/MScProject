#!/usr/bin/env 

##Author: Dale Housler
# This program checks if there are multiple conformation directories

import os

start_directory = os.getcwd()
os.chdir(start_directory)
conformation_dirs = []
conf_dir_match = ''

def checkForConformations(conformation_dirs, conf_dir_match):

    

    # this is the NOT set only want directories NOT files remove by file type .XXX
    notFile = ("pdb", "mol2", "csv", "txt", "py","kin","log","rsa")

    directories = [f for f in os.listdir(start_directory) if not  f.endswith(notFile)]
    #print(directories)
    conformation_dirs_match = (directories[-1])
    #print(conformation_dirs_match)
    for i in range(len(directories)):
        if len(directories[i]) == 4:
            conf_dir = (directories[i])
            #print(conf_dir)
            conf_dir_match = conf_dir[-3:]
            #print(conf_dir_match)
            
    if (conf_dir_match == conformation_dirs_match):
        main_lig_dir = conf_dir_match
            
        print("\nThere are multiple conformations of the ligand: " + main_lig_dir)
        print("Would you like to create the correctly merged conformation .pdb files?\n")

checkForConformations(conformation_dirs, conf_dir_match)
