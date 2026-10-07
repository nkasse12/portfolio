sleep = [7, 6, 8, 5, 7, 9]   

total = 0
for hours in sleep:
    total += hours

print("Total:", total)
print("Average:", round(total / len(sleep), 2)) 