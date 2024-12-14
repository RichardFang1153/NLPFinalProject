import sys

if (len(sys.argv) != 2):
    print("Not enough arguments")
else:
    file = open(sys.argv[1], "r")
    output = open("BILOU.txt", "w")

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
                    print(previous_split[0] + "\t" + "L-DATE", file=output)
                elif ((previous_2_split[1][0] in bio) and (previous_split[1][0] == "B") and ((split_line[1][0] == "O") or (split_line[1][0] == "B"))):
                    print(previous_split[0] + "\t" + "U-DATE", file=output)
                else:
                    print(previous, end = "", file=output)
            else:
                print(previous, end = "", file=output)
        else:
            print(previous, end = "", file=output)
        previous_2 = previous
        previous = line
        
        
    file.close()
    output.close()

#python3 bio-fixer.py [name_of_file] [addB or minusI]
#if you want to fix the organization results, make sure to change line 24 with this:
#print(previous_split[0] + "\t" + "B-ORGANIZATION", file=output)
