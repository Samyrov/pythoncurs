sum=int(input("Яку суму бажаєте зняти "))
notes = [500, 200, 100, 50, 20, 10] 
counts = [0] * len(notes) 
remainder = sum 

for i in range(len(notes)):
    if remainder == 0:
        break
    elif remainder < notes[i]:
        continue
    else:
        count = min(remainder // notes[i], 10) 
        counts[i] = count
        remainder -= count * notes[i]

if remainder > 0:
    print("Неможливо видати суму мінімальними банкнотами.")
else:
    print("Мінімальна кількість банкнот:")
    for i in range(len(notes)):
        if counts[i] > 0:
            print(str(notes[i]) + " x " + str(counts[i]))