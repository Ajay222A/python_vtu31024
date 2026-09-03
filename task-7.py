n = int(input("Enter number of items: "))
print("Enter elements: ")
arr = list(map(int, input().split()))
prefix_sum = []
total = 0
for num in arr:
    total += num
    prefix_sum.append(total)
print("prefix sum: ",end="")
for value in prefix_sum:
    print(value, end=" ")