#1. Kod
l=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
m = []
def flaten(x):
    for i in x:
        if type(i) == list:
            flaten(i)
        else:
            m.append(i)
flaten(l)
print(m)
[1, 'a', 'cat', 2, 3, 'dog', 4, 5]

#2.Kod
a = [[1, 2], [3, 4], [5, 6, 7]]
l=[]
for i in range(0,len(a)):
        a[i].reverse()
        l.append(a[i])
l.reverse()
print(l)
[[7, 6, 5], [4, 3], [2, 1]]

