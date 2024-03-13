import csv

def main():
    "Это основная функция, которая ничего не принимает на вход."
    newFile = open("students_new.csv", mode="w", newline="", encoding="utf-8")
    with open("students.csv", encoding="utf-8") as csvData:
        csvReader = csv.reader(csvData)
        csvList = list(csvReader)
        csvNew = csvList
        # print(list(csvReader)[1])
        nonBrokenAmount = 0
        avgOut = 0
        writer = csv.writer(newFile)
        writer.writerow(["id", "Name", "titleProject_id", "class", "score"])

        for j in range(1, len(csvList)):
            enlist = csvList[j]
            if enlist[4] != "None":
                nonBrokenAmount += 1
                avgOut += int(enlist[4])
        avgOut = round(avgOut / nonBrokenAmount, 3)

        for i in range(1, len(csvList)):
            csvNew[i] = csvList[i]
            if csvList[i][4] == "None":
                csvNew[i][4] = avgOut
            if "Хадаров Владимир" in csvList[i][1]:
                print(f"Ты получил: {csvList[i][4]}, за проект - {csvList[i][2]}")
            writer.writerow(csvNew[i])

        
if __name__ == "__main__": main()
    