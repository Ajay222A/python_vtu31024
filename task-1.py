import heapq

st=[1,4,6,7,9]
heapq.heapify(st)
max=st[-1]
min=0
print(st)
for item in st:
    if item<max and min<item:
        min=item
if max==0:
    print("-1")
else:
    print(min)
