#!/usr/bin/env python
#Author: Dale Housler
#OS: UNIX & WINDOWS
# CountResidues.py

#This program counts the number of residues in the split PDB files
#Used as a quick test to see if chains are the same length


import os # runs os commands
import re # regular expressions

def countResidues():
    start_directory = os.getcwd()

    directories = [f for f in os.listdir(start_directory) if  f.endswith(".pdb")]
    print("PDB Files present in current directory: \n")

    i = 1
    count = 0

    #prints pdb files in the directory
    for i in range(0,len(directories)):
        print(str(directories[i]))

    print("\n'ATOM': residue count per pdb file: ")
    #Shows line count per pdb file and converts at least 24 to .mol2
    
    for i in range(0,len(directories)): #loops per file in directory
        pdb_files = (directories[i])
        mol_f = re.sub('.pdb','',pdb_files)#removed.pdb file format for mol2 naming

    ###way 1 Count all alpha carbons
        with open(pdb_files) as h: #counts each line per pdb file
            for line in h:
                if ("ATOM" in line) and ("REMARK" not in line) and ("HETNAM" not in line) and ("REVDAT" not in line):
                    line_array = re.split('\s+', line) #split on the space to find the columns
                    if "CA" in line_array[2]: #USE CA not N as other side chain N's picked up 
                        count += 1

        #prints the count    
        if (count > 0) and (count <= 24):
            print(str(pdb_files) + ": [" + str(count) + "] Possible **peptide ligands converted to .mol2 files")
        else:
            print(str(pdb_files) + ": [" + str(count) + "]")
       
        count = 0 #set count back to zero for next file count
###END DEF  
countResidues()
