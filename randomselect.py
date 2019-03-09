filename = '1007result'
file = open(filename + '.txt')
f1 = open(filename + '%90.txt','w+')
f2 = open(filename + '%10.txt','w+')
line = file.readline()
n = 0
while line:
    n = n+1
    if n % 10 == 0:
        f2.write(line)
    else:
        f1.write(line)
    line = file.readline()
f2.close()
f1.close()
file.close()
    