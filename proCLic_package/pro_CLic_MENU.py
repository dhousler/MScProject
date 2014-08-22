#!/usr/bin/env python

#Author: Dale Housler
#Date: 10-10-2013
#OS: UNIX
#Program Description: This file should run the os commands

#Last updated: 13-04-2014

#Open each PDB directory of interest (manually)

#Make sure ('export LD_LIBRARY_PATH=/usr/local/lib') is typed at the command
#prompt if running python3.3  and openbabel (applies to chain separate program)

#In this directory:
#run the Chain separate program and store it in this directory
#run the proACT2.py program and save the files in the proACT_run directory
#run the contacts.py program and store the number of polar apolar bonds

import os
from os import listdir
from os.path import isfile,isdir
import shutil #allows files to be copied or moved between dirs
import sys # Allows exit for error messages

#os.system('python3.3 /root/Scorpio2_PDB_Files/SetLibPath.py') # runs the external script to set the library and allow openbabel to run in python3.3 env.

start_directory = os.getcwd()

### Removes the PDB file needed by chimera if option 2 selected
def removePDBRemnants():
    
    PDB_dir = os.chdir('/root/proCLic_package/')
    #print(PDB_dir)
    PDBfile = [f for f in os.listdir(PDB_dir) if f.endswith(".pdb")]
    if len(PDBfile) > 0:
        i = 0
        for i in range(len(PDBfile)):
            if (len(PDBfile[i])) == 8:
                os.remove(PDBfile[i])
            i+=1
    os.chdir(start_directory)
###

def CheckMultiLigDirs():
    start_directory = os.getcwd()
    notFile = ("pdb", "mol2", "csv", "txt", "py","kin","log","rsa") # this is the NOT set only want directories NOT files remove by file type .XXX

    #Get the ligand directories
    directories = [f for f in os.listdir(start_directory) if not f.endswith(notFile)]
    dirLength = len(directories)
    if dirLength > 0:
      for i in range(0,dirLength):
          if len(directories[i]) > 1:
            print("There are multiple ligand directories, You can either: ")
            print("1. Change dir (cd) to the ligand of interest manually, or")
            print("2. Loop through each ligand directory automatically.")
            choice = input()
            if choice == "1":
                sys.exit(1)
            if choice == "2":
                os.system('python3.3 /root/proCLic_package/NavigateLigandDirs.py')
            else:
                print("Invalid Seletion.")
                sys.exit(1)


loop = False
if (loop == False):
    ###PROGRAM MENU###
    print("\nPROGRAM MENU")
    print("1. Run Chain Separate on the PDB file.\n2. Run Chimera.\n3. Run Directory Manager.\n4. Generate pro_CLic counts - Active Site.\n5. Generate pro_CLic counts - Change Unbound to Bound.\n")
    print("MISCELLANEOUS PROGRAMS")
    print("I.    Count Residues\nII.   Mol2 Fixer\nIII.  Create Conformation Directories\n")
    print("q to quit")
    menu = input()

    path = os.getcwd()

    ###Run chain separate program###
    if (menu == "1"):
        removePDBRemnants()
        os.chdir(path)
        os.system('python3.3 /root/proCLic_package/ChainSeparate2PDB_PtnLigUNIX_dir.py')
    #else:
    #    loop = True

    ###Run Chimera###
    if (menu == "2"):
       #This runs chimera
        ###Go into the pdb dir copy the original pdb file, dump it in the pro_CLic packages folder
        PDB_dir = os.getcwd()
        print(PDB_dir)
        os.chdir(path)
        PDBfile = [f for f in os.listdir(PDB_dir) if f.endswith(".pdb")]

        i = 0
        for i in range(len(PDBfile)):
            if (len(PDBfile[i])) == 8:
                shutil.copy(PDBfile[i],'/root/proCLic_package/')
            i += 1
            
        #RUN CHIMERA
        os.chdir ('/root/chimera/bin/')
        os.system('./chimera --nogui /root/proCLic_package/importPDB.py')

        #remove the pdb file from the proCLic_Package folder
        
    ###Run Directory Manager###
    if (menu == "3"):
        removePDBRemnants()
        os.chdir(path)
        CheckMultiLigDirs()
        os.system ('python3.3 /root/proCLic_package/DirectoryManagerTypeIII.py')

    ### Run the binding waters program to get the Polar Apolar bond counts, the HOH binding water counts and generate the log file ###
    if (menu == "4"):
        removePDBRemnants()
        os.chdir(path)
        CheckMultiLigDirs()
        os.system ('python3.3 /root/proCLic_package/pro_CLic_runDirectories.py')

    if (menu == "5"):
        os.chdir(path)
        os.system('python3.3 /root/proCLic_package/Phase2/ChangeInContactsLog.py')

    ####################
    ###MISCELLANEOUS####

    if (menu == "i") or (menu == "I") :
        os.chdir(path)
        os.system('python3.3 /root/proCLic_package/Misc/CountResidues.py')

    if (menu == "ii") or (menu == "II"):
        os.chdir(path)
        os.system('python3.3 /root/proCLic_package/Misc/Mol2Fixer.py')

    if (menu == "iii") or (menu == "III"):
        os.chdir(path)
        os.system('python3.3 /root/proCLic_package/Misc/conformationFolders.py')

    ####################

          
    else:
        loop = True
