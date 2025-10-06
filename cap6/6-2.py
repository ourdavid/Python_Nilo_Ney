l = [1,2,3,4,5]
l2 = [6,7,8,8,9,10]
l3 = []
x = 0

while x < len(l):
    l3.append(l[x])
    x += 1

x = 0
while x < len(l2):
    l3.append(l2[x])
    x += 1

print(l3)

