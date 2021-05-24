d = {'vishal':[10,20,30],'dinesh':[30,40,50],'abhihek':[10,15,5]}
d1 = {}
for i in d.items():
    a = sum(i[1])
    d1[i[0]] = a
a = sorted(d1.items(), key=lambda x:x[1])

print("Topper is",a[-1][0],"Marks Score",a[-1][1])
