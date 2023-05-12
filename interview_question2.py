m = int(input('Input the total number of people (1~100) : '))
p = []
out = 0
index = 0
if(m>0 and m<=100):
    for i in range(1,m+1):
        p.append(i)
    while(len(p) > 1):
        out += 1
        index += 1
        if (index > len(p)):
            index = 1
        if(out == 3):
            out = 0
            p.pop(index-1)
            index -= 1
    print("The Last No. is", p[0])
else:
    print(m, "This number is out of range.")