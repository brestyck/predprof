import csv

def main():
    "Это основная функция, которая ничего не принимает на вход."
    with open("students_new.csv", encoding="utf-8") as csvData:
        csvData = csv.reader(csvData)
        csvList = list(csvData)
        for j in range(1, len(csvList)):
            csvList[j][4] = float(csvList[j][4])

        for i in range(2, len(csvList)-1):
            print(f"\033[101m{i} \033[42m{csvList[i]}\033[49m")
            print(f"\033[101m{i+1} \033[42m{csvList[i+1]}\033[49m")
            key = csvList[i][4]
            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i-1
            # (print(key, type(key), csvList[j][4], type(csvList[j][4])) or True)
            while j >= 0 and key < csvList[j][4]:
                    csvList[j + 1] = csvList[j]
                    j -= 1
            csvList[j + 1][4] = key
    amtAnswered = 1
    for y in range(2, len(csvList)-1):
        x = csvList[y]
        if "10" in x[3]:
            name_splt = x[1].split()
            print(f"{amtAnswered} место: {name_splt[1][0]}. {name_splt[0]}")
            amtAnswered += 1
            csvList.pop(y)
if __name__ == "__main__": main()
