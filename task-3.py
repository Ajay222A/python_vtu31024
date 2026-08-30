n=[
    ["Ajay",25],
    ["Yaswanth",30],
    ["Pratheek",35],
    ["Rakesh",40]
]
age=25
age_limit=[]
lower_case=[]
print("**********Before sorting**********")
for i in n:
    print(f"\t{i[0]} : {i[1]}")
n.sort()
for i in n:
    if i[1]>age:
        age_limit.append([i[0],i[1]])
    lower_case.append(i[0])
upper_case=list(map(lambda x:x.upper(),lower_case))
print("\n**********After sorting**********")
for i in n:
    print(f'\t{i[0]} : {i[1]}')
print(f"\n**********Older than {age} age group**********")
for i in age_limit:
    print(f"\t{i[0]} : {i[1]}")
print(f"\n**********Upper case **********")
for i in upper_case:
    print(f"\t{i}")