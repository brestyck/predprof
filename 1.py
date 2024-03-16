import csv

fhook = open(r"C:\Users\Kids01\Desktop\Вариант 5\vacancy_new.csv", encoding="utf-8").readlines()
fcsv = [i.split(";") for i in fhook]
fneu = []
fcsv.pop(0)

for j in fcsv:
	fneu.append(j)

fcsv.sort(key=lambda a: int(a[2]))
fcsv = fcsv[::-1]

a = fcsv[0]
b = fcsv[1]
c = fcsv[2]

print(f"{a[0]} - {a[1]} - {a[2].strip()}")
print(f"{b[0]} - {b[1]} - {b[2].strip()}")
print(f"{c[0]} - {c[1]} - {c[2].strip()}")
