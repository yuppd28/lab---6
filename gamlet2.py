import csv
zag=0
pr=0
my_list=[]
filename = "gamlet.txt"
fd=open(filename, "r")


for row in fd:
    pr=pr+row.count(' ')
    zag=zag+len(row)
    slova=row.split(" ")
    my_list.append(slova)
    print(row)

fd.close()
print(zag)
print(pr)
print("slova=",len(my_list))

