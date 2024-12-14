import sys

if (len(sys.argv) != 4):
    print("Not enough arguments")
else:
    file = open(sys.argv[1], "r")
    output = open("BILOU.txt", "w")
    category = sys.argv[3]
    if (sys.argv[2] == "dev"):
        previous_2 = ""
        previous = ""
        bio = "BIO"
        for line in file:
            if (not line.isspace()):
                split_line = line.split()
                previous_2_split = previous_2.split()
                previous_split = previous.split()
                if ((len(previous_2_split) == 2) and (len(previous_split) == 2)):
                    if (((previous_2_split[1][0] == "I") or (previous_2_split[1][0] == "B")) and (previous_split[1][0] == "I") and ((split_line[1][0] == "O") or (split_line[1][0] == "B"))):
                        print(previous_split[0] + "\t" + "L-" + category, file=output)
                    elif ((previous_2_split[1][0] in bio) and (previous_split[1][0] == "B") and ((split_line[1][0] == "O") or (split_line[1][0] == "B"))):
                        print(previous_split[0] + "\t" + "U-" + category, file=output)
                    else:
                        print(previous, end = "", file=output)
                elif ((len(previous_2_split) != 2) and (len(previous_split) == 2)):
                    if ((previous_split[1][0] == "B") and ((split_line[1][0] == "O") or (split_line[1][0] == "B"))):
                        print(previous_split[0] + "\t" + "U-" + category, file=output)
                    else:
                        print(previous, end = "", file=output)
                else:
                    print(previous, end = "", file=output)
            else:
                previous_split = previous.split()
                if (previous_split[1][0] == "B"):
                    print(previous_split[0] + "\t" + "U-" + category, file=output)
                else:
                    print(previous, end = "", file=output)
            previous_2 = previous
            previous = line
        print("", file=output)
  
    elif (sys.argv[2] == "training"):
        previous_2 = ""
        previous = ""
        bio = "BIO"
        for line in file:
            if (not line.isspace()):
                split_line = line.split()
                previous_2_split = previous_2.split()
                previous_split = previous.split()
                if ((len(previous_2_split) == 3) and (len(previous_split) == 3)):
                    if (((previous_2_split[2][0] == "I") or (previous_2_split[2][0] == "B")) and (previous_split[2][0] == "I") and ((split_line[2][0] == "O") or (split_line[2][0] == "B"))):
                        print(previous_split[0] + "\t" + previous_split[1] + "\t" + "L-" + category, file=output)
                    elif ((previous_2_split[2][0] in bio) and (previous_split[2][0] == "B") and ((split_line[2][0] == "O") or (split_line[2][0] == "B"))):
                        print(previous_split[0] + "\t" + previous_split[1] + "\t" + "U-" + category", file=output)
                    else:
                        print(previous, end = "", file=output)
                elif ((len(previous_2_split) != 3) and (len(previous_split) == 3)):
                    if ((previous_split[2][0] == "B") and ((split_line[2][0] == "O") or (split_line[2][0] == "B"))):
                        print(previous_split[0] + "\t" + previous_split[1] + "\t" + "U-" + category, file=output)
                    else:
                        print(previous, end = "", file=output)
                else:
                    print(previous, end = "", file=output)
            else:
                previous_split = previous.split()
                if (previous_split[2][0] == "B"):
                    print(previous_split[0] + "\t" + previous_split[1] + "\t" + "U-" + category, file=output)
                else:
                    print(previous, end = "", file=output)
            previous_2 = previous
            previous = line
        print("", file=output)

    file.close()
    output.close()

