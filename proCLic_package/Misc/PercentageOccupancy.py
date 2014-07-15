import os

captureLine = []
capture_set = ()
captureLine_set = ()

start_directory = os.getcwd()
pdb_files = [f for f in os.listdir(start_directory) if  f.endswith(".pdb")]
for i in range(len(pdb_files)):
    print(pdb_files[i])

pdb_file = input("\nEnter the .pdb file to use from the selection above: \n")
#print (pdb_file)

with open(pdb_file, 'r') as readfile:
    for line in readfile:
      
        moleculeRef = line[16:26]
        perc = line[55:60]
        store = ''

        if store != perc:

            captureLine += [moleculeRef + ": " + perc]
            store = perc

captureLine_set = set(captureLine)
#print(captureLine_set)
captureLine_List = list(captureLine_set)
#print(captureLine_List)
captureLine_List_sort = sorted(captureLine_List)

print("\nPercentage abundance (Occupancy): \n")

for i in range(len(captureLine_List_sort)):
    print(captureLine_List_sort[i])

readfile.close()
