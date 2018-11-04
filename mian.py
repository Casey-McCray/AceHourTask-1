'''SAMPLE INPUT
5
56
98
23
47
32
76
23
87
23
86
45
87
34
76
45
76
88
13
12
34'''

subs = ['English', 'Maths', 'History', 'Science']
num = int(input())
table = []

for i in range(num):   
    dic = {}
    for j in range(len(subs)):
        dic[subs[j]] = int(input())
    table.append(dic)
        
for i in range(num):
    q = table[i].values()
    percentage = sum(q)/4
    print("Student" + str(i+1) + ": " + str(percentage))
    
for i in range(len(subs)):
    l = []
    for j in range(num):
        l.append(table[j][subs[i]])
    print("Top Scorer of " + subs[i] + " is Student" + str(l.index(max(l)) + 1))

