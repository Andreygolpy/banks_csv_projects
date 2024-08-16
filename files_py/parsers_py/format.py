f = open("input.csv", 'r')
o = open("output.csv", 'w')
a = f.readlines()
b = [a[0]]
n = len(a)
#24975 382501
x = "382501"
for i in range(1, n):
    if(a[i][:len(x)] != x):
        b[-1] += a[i]
    else:
        b.append(a[i])
        x = str(int(x) + 1)
    if(i % 1000 == 0):
        print(i)
a = b
n = len(a)
x = "-1"
a[0] = a[0].replace(',', '\t')
o.write(a[0])
for i in range(1, n):
    a[i] = a[i].replace('\n', '')
    a[i] = a[i].replace(',', '\t', 2)
    a[i] = a[i].replace('\t', "17041975")
    a[i] = a[i].replace("17041975", '\t', 2)
    if(a[i][a[i].find('\t') + 1] == '3' or a[i][a[i].find('\t') + 1] == '\t'):
        continue
    x = str(int(x) + 1)
    if(int(a[i][a[i].find('\t') + 1]) > 3):
        a[i] = x + "\tPositive" + a[i][a[i].find('\t') + 2:]
    else:
        a[i] = x + "\tNegative" + a[i][a[i].find('\t') + 2:]
    f1 = False
    f = False
    s = ""
    for j in range(len(a[i])):
         if(a[i][j] == '<'):
             f = True
         if(a[i][j] == '['):
             f1 = True
         if(not f and ord(a[i][j]) < 2000 and not f1):
             s += (a[i][j])
         if(a[i][j] == '>'):
             f = False
         if(a[i][j] == ']'):
             f1 = False
    a[i] = s.replace('>', '')
    a[i] = s.replace(']', '')
    if(a[i].find('"') == a[i].find('\t', a[i].find('\t') + 1) + 1):
        a[i] = a[i][:a[i].find('"')] + a[i][a[i].find('"') + 1:-1] + '\n'
    else:
        a[i] += '\n'
    o.write(a[i])
    if(i % 1000 == 0):
        print(i)
o.close()
