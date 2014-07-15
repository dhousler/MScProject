#!/usr/bin/env python

# Author: Dale Housler
# Date: 09-06-2014
# Python: 3.3
# LogfileRformatCorrelations.py
# Program to write the log file in a form for R correlation

#Uses a log file of contact counts:' Log_XPDB.csv'
#Writes to the 'R_ContactCorrelations.txt' file

### Reference ###
#http://www.pythonforbeginners.com/systems-programming/using-the-csv-module-in-python/
###

import os
import operator
import csv
import re


start_directory = os.getcwd()
LogFile = [f for f in os.listdir(start_directory) if f.endswith('.csv')]

ReadFile = LogFile[0]
#print (ReadFile)
PDB_LogFile = [f for f in os.listdir(start_directory) if f.endswith('.pdb')]
PDB_ref = PDB_LogFile[0]
PDB_ref = PDB_ref[:4].strip() #strip first 5 to get pdb ref


file = open("R_ContactCorrelations_" + PDB_ref + ".txt", "w")
file.write("###This information can be read by R program to draw correlations###\n\n")

def writeR_Code(i,ligAx_str,ligBy_str):
    #Polar column 3
    if i == 3:
        PA = ("P.A <- c(" + ligAx_str + ")")
        PB = ("P.B <- c(" + ligBy_str + ")")
        print("\n" + PA)
        file.write("#Polar Contacts Count: \n")
        file.write(PA + "\n")
        print(PB)
        file.write(PB + "\n")
        print('plot(P.A,P.B, pch=19, col="green")')
        file.write('plot(P.A,P.B, pch=19, col="green")' + "\n\n")
    #Apolar column 4
    if i == 4:
        APA = ("AP.A <- c(" + ligAx_str + ")")
        APB = ("AP.B <- c(" + ligBy_str + ")") 
        print("\n" + APA)
        file.write("#Apolar Contacts Count: \n")
        file.write(APA + "\n")
        print(APB)
        file.write(APB + "\n")
        print('points(AP.A,AP.B, pch=19, col="purple")')
        file.write('points(AP.A,AP.B, pch=19, col="purple")' + "\n\n")
        #Binding Waters column 5
    if i == 5:
        BWA = ("BW.A <- c(" + ligAx_str + ")")
        BWB = ("BW.B <- c(" + ligBy_str + ")") 
        print("\n" + BWA)
        file.write("#Binding Water Count: \n")
        file.write(BWA + "\n")
        print(BWB)
        file.write(BWB + "\n")
        print('points(BW.A,BW.B, col="blue")')
        file.write('points(BW.A,BW.B, col="blue")'+ "\n\n")

def Alt_Chain(ReadFile):

    ligAx = []
    ligBy = []
    ligAxTransposed = []
    ligByTransposed = []

    file.write("## This set shows the Main Chain correlations: ##\n\n")

    i = 3 #starts at the third position (i.e., column3)
    while i <= 5:
   
        with open(ReadFile) as h:
            reader = csv.reader(h)
            rownum = 0
            n = 1
       
            for row in reader:
                #print(i)
                if rownum == 0:
                    header = row
                #Capture Even Row
                elif n == rownum:
                    ligAx += [row[i]]
                    n +=2 # for chain A_A, A_B set n+=2
                   #Capture Odd Row
                elif n == rownum + 1:
                    ligBy += [row[i]]
          
                rownum += 1

            #print(ligAx)
            #print(ligBy)
            j = 0
            while j < (len(ligAx)):

                tx = [ligAx[j]]
                #print(ligAx[j])
                ty = [ligBy[j]]
                #print(ligBy[j])
                ligAxTransposed += tx
                ligAxTransposed += ty
                j += 2

            #print(ligAxTransposed)
            tx = []
            ty = []
               
            k = 0
            while k < (len(ligAx)):

                ty = [ligBy[k+1]]
                #print(ligBy[k+1])
                tx = [ligAx[k+1]]
                #print(ligAx[k+1])
                ligByTransposed += tx
                ligByTransposed += ty
                k += 2

            #print(ligByTransposed)


            ligAxT = ligAxTransposed
            ligByT = ligByTransposed
       
       
            ## Convert Ligand A's capture to the form read by r
            ligAx_str = str(ligAxT)
            ligAx_str = re.sub('[\'\[\]]','',ligAx_str)
       

            ## Convert Ligand B's capture to the form read by r
            ligBy_str = str(ligByT)
            ligBy_str = re.sub('[\'\[\]]','',ligBy_str)

            writeR_Code(i,ligAx_str,ligBy_str)

            #Clear array contents to allow for next column
            ligAx = []
            ligBy = []

            ligAxTransposed = []
            ligByTransposed = []
       

            i += 1
###End Def

def Alt_Lig(ReadFile):

    ligAx = []
    ligBy = []
   
    file.write("## This set shows the Alternative Chain, i.e., ligand correlations: ##\n\n")
   
    i = 3 #starts at the third position (i.e., column3)
    while i <= 5:
   
        with open(ReadFile) as h:
            reader = csv.reader(h)
            rownum = 0
            n = 1
       
            for row in reader:
                #print(i)
                if rownum == 0:
                    header = row
                #Capture Even Row
                elif n == rownum:
                    ligAx += [row[i]]
                    n +=2 # for chain A_A, A_B set n+=2
                   #Capture Odd Row
                elif n == rownum + 1:
                    ligBy += [row[i]]
          
                rownum += 1
      
       
            ## Convert Ligand A's capture to the form read by r
            ligAx_str = str(ligAx)
            ligAx_str = re.sub('[\'\[\]]','',ligAx_str)
       

            ## Convert Ligand B's capture to the form read by r
            ligBy_str = str(ligBy)
            ligBy_str = re.sub('[\'\[\]]','',ligBy_str)
           
            writeR_Code(i,ligAx_str,ligBy_str)

            #Clear array contents to allow for next column
            ligAx = []
            ligBy = []
       

            i += 1
    file.close()

Alt_Chain(ReadFile) # Alternates A_A, B_A
Alt_Lig(ReadFile) # Alternates A_A, A_B
