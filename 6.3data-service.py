import csv
zag=0
pr=0
my_list=[]
my_list1=[]
filename="gamlet.txt"

fd=open(filename,'r')
for row in fd:
    pr=pr+row.count(' ')
    zag=zag+len(row)
    word=row.split(' ')
    my_list.append(word)
    print(row)

fd.close()
print(zag)
print(pr)
print('word=',len(my_list))

L=len(my_list)
L1=0
all_word=0
word_uniq=0
for i in range (L):
    L1=len(my_list[i])
    for j in range (L1):
        elem=my_list[i][j]
        all_word=all_word+1
        if elem in my_list1:
            continue
        else:
           my_list1.append(elem)
word_uniq=len(my_list1)
print('all_word=', all_word)
print('word_uniq=', word_uniq)