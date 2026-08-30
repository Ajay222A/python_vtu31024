from datetime import datetime

print("Enter how many events you have:")
n = int(input())
events = []
for _ in range(n):
    name, date_str = input("Enter event name and date").split()
    date = datetime.strptime(date_str, "%Y-%m-%d")
    events.append((name, date))
month = int(input("Enter month number"))
events.sort(key=lambda x: x[1])
for event in events:
    print(event[0], end="")
print()
print(events[0][0])
print(events[-1][0])
for event in events:
    if event[1].month == month:
        print(event[0], end="")
