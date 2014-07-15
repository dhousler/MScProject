#!/usr/bin/env python

#Author: Dale Housler
#Date: 12-11-2013
#OS: UNIX
#Program Description: This program allows the user to open a chimera session, either in 
#the command prompt or as a GUI (Graphical User Interface)

##### REFERENCE #####
#UCSF Chimera--a visualization system for exploratory research and analysis. Pettersen EF, Goddard TD, Huang CC, Couch GS, Greenblatt DM, Meng EC, Ferrin TE. J Comput Chem. 2004 Oct;25(13):1605-12. 
#####################

#Note: runs python2 for chimera (Hence, raw_input used for user input#

import chimera
import os

from chimera import runCommand


start_directory = os.getcwd()

PDB_ref = raw_input("Enter the PDB ref to fetch: ") #raw_input as uses python 2
#PDB_full = PDB_ref + ".pdb"
#openModels = chimera.openModels.open(PDB_full, type="PDB") #opens chimera gui

PDB_full = "open " +  PDB_ref + ".pdb"
runCommand(PDB_full)

chimeraOption = str(raw_input("Would you like to run chimera in:\n(N)-Nogui mode or,\n(G)-Gui mode?\n")).upper()


###OPENS CHIMERA WITHOUT GUI###
if (chimeraOption == "N"): 
	print ("\nEnter chimera commands e.g.:\ncolor blue :tyr \nType save image (to save), \nType close (to refresh), \nType 'stop' to end.")
	
	os.system('/root/chimera/bin/chimera --nogui')

###OPENS CHIMERA###
elif (chimeraOption == "G"):
	os.chdir ('/root/chimera/bin/')
	os.system ('./chimera')
else:
	print ("Exit Chimera")
	
#Loops Menu again
os.chdir(start_directory)

## Removes the PDB file needed by chimera for the run
PDB_dir = os.getcwd()
print(PDB_dir)
PDBfile = [f for f in os.listdir(PDB_dir) if f.endswith(".pdb")]

i = 0
for i in range(len(PDBfile)):
        if (len(PDBfile[i])) == 8:
                os.remove(PDBfile[i])
        i+=1
###

os.system('python3.3 /root/proCLic_package/pro_CLic_MENU.py')
