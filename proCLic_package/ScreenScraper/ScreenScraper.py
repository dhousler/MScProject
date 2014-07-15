#!/usr/bin/env python

#Author: Dale Housler
#Original programs created 21-06-2013
#Updated 12-06-2014
#ScorpioPDB_ScreenScraper.py

#This program accessed the scorpio2.biophysics.ismb.lon.ac.uk site
#Downloads the pages with the ITC pdb dataset
#Scrapes these downloaded pages for the pdb references
#Saves the found references to a txt.file
#Reads this text file and accessed the protein databank http://www.rcsb.org/pdb/files/
#Copies the PDB infor into a .pdb file and saves these to a PDB_Files directory
#Once this has been complete it creates and moves all files into a relevant pdb directory

import urllib
from urllib.request import urlopen
import datetime
import os
import operator
import re
import shutil

now = datetime.datetime.now()
now_str = now.strftime("%Y-%m-%d")

if not os.path.exists('PDB_Files'):
    os.makedirs('PDB_Files')


def Scrape_Scorpio2(now_str):
    ###NOTE: PG numbers would need to be increased if more structures are added, or this part of the code converted to a loop
    ####Page1###
    pg1 = urlopen ("http://scorpio2.biophysics.ismb.lon.ac.uk/structure/browse?page=1")
    p1 = pg1.read().decode('utf-8')
    #print (p1)

    ###Page2###
    pg2 = urlopen ("http://scorpio2.biophysics.ismb.lon.ac.uk/structure/browse?page=2")
    p2 = pg2.read().decode('utf-8')
    #print (p2)

    ###Page3###
    pg3 = urlopen ("http://scorpio2.biophysics.ismb.lon.ac.uk/structure/browse?page=3")
    p3 = pg3.read().decode('utf-8')
    #print (p3)

    ###Page4###
    pg4 = urlopen ("http://scorpio2.biophysics.ismb.lon.ac.uk/structure/browse?page=4")
    p4 = pg4.read().decode('utf-8')
    #print (p4)

    ###Page5###
    pg5 = urlopen ("http://scorpio2.biophysics.ismb.lon.ac.uk/structure/browse?page=5")
    p5 = pg5.read().decode('utf-8')
    #print (p5)

    ###Page6###
    pg6 = urlopen ("http://scorpio2.biophysics.ismb.lon.ac.uk/structure/browse?page=6")
    p6 = pg6.read().decode('utf-8')
    #print (p6)

    #saveFile = input("Enter the file name: ")
    #f = open(saveFile + ".txt" , "a+")
    saveFile = ("Scorpio2_HTML_Scrape.txt")
    print(saveFile)
    f = open('{}_Scorpio2_HTML_Scrape.txt'.format(now_str), 'w+')
   
    f.write('********************PAGE01********************')
    f.write(p1)
    f.write('********************PAGE02********************')
    f.write(p2)
    f.write('********************PAGE03********************')
    f.write(p3)
    f.write('********************PAGE04********************')
    f.write(p4)
    f.write('********************PAGE05********************')
    f.write(p5)
    f.write('********************PAGE06********************')
    f.write(p6)
    f.close()

###END DEF

def ExtractPDB_references():
    inputFile = ('{}_Scorpio2_HTML_Scrape.txt'.format(now_str))
    outputFile =('{}_Scorpio2_Scrape_PDBrefs.txt'.format(now_str))
    x = 'Id='
    counter = 0
    f = open(inputFile)
    #f = open('C:/Dale/Python/Project/Scorpio2_HTML_PDB_FINDER/Scorpio_pagesALL_py3.txt')
    for line in f:
      if x in line:
        counter += 1
        matches = line [-14:-10]
        #on screen
        print (matches)
        #in file
        g = open(outputFile, 'a+')
        #f = open('C:/Dale/Python/Project/Scorpio2_HTML_PDB_FINDER/Scorpio_PDBrefsALL_py3.txt', 'a+')
        g.write(matches + '\n')
        g.close()
    f.close()

    # COUNT

    #on screen
    print ("Total count: " + str(counter))

    #in file
    #h = open(outputFile, 'a+')
    #f = open('C:/Dale/Python/Project/Scorpio2_HTML_PDB_FINDER/Scorpio_PDBrefsALL_py3.txt', 'a+')
    #h.write ("Total count: " + str(counter))
    #h.close()
###END DEF

def FetchPDBrefs_fromPDB():
    f = open('{}_Scorpio2_Scrape_PDBrefs.txt'.format(now_str))
    i = 1
    for line in f:
        PDB_Code = line [0:4] # this strips /n off
        geturl = 'http://www.rcsb.org/pdb/files/' + PDB_Code +'.pdb' #sets PDB URL pg
       
        saveurl_file = "PDB_Files/" + PDB_Code + ".pdb"

        # Accesses the PDB
        site = urllib.request.urlopen(geturl)
        data = site.read()
        data_str = str(data,'UTF-8')
        file = open(saveurl_file,"a+") #open file in binary mode
        file.write(data_str)
        file.close()

        #Tells user that the file has been saved from the PDB website to the txt file
        print (str(i) + ". " + '[' + PDB_Code + ']' + ' file saved to ' + saveurl_file)
        i += 1
###END DEF

def MovePDB_files():
    os.chdir('PDB_Files')
    pdbDir = os.getcwd()
    print(pdbDir)
    pdb_files = [f for f in os.listdir(pdbDir) if f.endswith('.pdb')]

    i = 0
    for i in range(len(pdb_files)):
        pdb_dir = str(pdb_files[i])
        pdb_dir = re.sub('.pdb','',pdb_dir)
        if not os.path.exists(pdb_dir):
            os.makedirs(pdb_dir)
            shutil.move(pdb_files[i], pdb_dir)
###END DEF

# 1. Scrape Scorpti2 Website, collect HTML pages with PDB references
Scrape_Scorpio2(now_str)
# 2. Searches the dated Scorpio2_HTML_Scrape.txt file and finds the PDB references and writes to file
ExtractPDB_references()
# 3. Looks in the dated Scorpio2_Scrape_PDBrefs,txt file and uses this to fetch all PDB refs from the PDB online
FetchPDBrefs_fromPDB()
# 4. Moves all .pdb files into their own directories
MovePDB_files()

print ('Saved successfully!')
