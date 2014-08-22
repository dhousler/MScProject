#!/usr/bin/env python

#Author: Dale Housler
#Mol2Fixer

#This program removes any character between columns 6 and 7 in the .mol2 file where a space is expected
#This program is run from the misc proCLic menu if proACT2 show as 'Value Error'

import os
import shutil
import sys
import string

start_directory = os.getcwd()

mol2_files = [f for f in os.listdir(start_directory) if f.endswith('.mol2')]

for i in range(len(mol2_files)):
    print(mol2_files[i])

mol2 = input("\nEnter the mol2 file to be converted: ")
    

IN = mol2
OUT = mol2
NEW = "new.mol2"
outfile = open(NEW, 'a+')


with open(IN, 'r') as readfile:
    for line in readfile:
        # Checks for the conformation letter at pos 15 and replace with ''
        #line = line.lstrip()
        if line[51:52] != ' ' and (".pdb" not in line):
            #print(line[51:52])
            new = list(line)
            new[51:52] = ' '
            #print(new)
            if new[-1] == ' ': #removes last element in the list if ' '
                del new[-1]
            newline = ''.join(new)
            #print(newline)
            outfile.write(newline)
        else:
            outfile.write(line)
                   
readfile.close()
outfile.close()

shutil.copy2(NEW, IN)
os.remove(NEW)

