import csv

def txt_to_csv(rsc: str):
    f = open(rsc, "r", newline="")
    g = open("results.csv", "w", newline="")

    for line in f.readlines():
        new_line = ""
        for item in line.split(" "):
            new_line = new_line + item + ","
        g.write(new_line.rstrip(","))

    f.close()
    g.close()


if __name__ == "__main__":

    infos = []
    f = open("infos.txt", "r", newline="")
    for line in f.readlines():
        infos.append(line.strip())
    f.close()

    prices = []
    f = open("prices.txt", "r", newline="")
    for line in f.readlines():
        prices.append(line.strip())
    f.close()

    i = 0
    results = []
    while i < len(infos):
        result = infos[i] + " " + prices[i]
        results.append(result)
        i = i + 1

    f = open("results.txt", "w", newline="")
    for result in results:
        f.write(result + "\n")
    f.close()

    txt_to_csv("results.txt")

