def tuple_required(filename):
   fin = open(filename,'r')
   for line in fin:
     line=line.split(",")
     tp=(line[2],line[3],line[6],line[7])
     print(tp)

fin = open('Street_Centrelines.csv','r')
print(tuple_required('Street_Centrelines.csv'))
