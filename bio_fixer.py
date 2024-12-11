import sys

if (len(sys.argv) != 3):
    print("Not enough arguments")
else:
    file = open(sys.argv[1], "r")
    output = open("fixedBIO.txt", "w")
    
    if (sys.argv[2] == "addB"):
        previous = ""
        inside_bio = "false"
        for line in file:
            if (not line.isspace()):
                split_line = line.split()
                if (split_line[1][0] == "B"):
                    inside_bio = "true"
                    print(previous, end = "", file=output)
                if (split_line[1][0] == "O"):
                    inside_bio = "false"
                    print(previous, end = "", file=output)
                if (split_line[1][0] == "I"):
                    if (inside_bio == "false"):
                        if (not previous.isspace()):
                            previous_split = previous.split()
                            print(previous_split[0] + "\t" + "B-DATE", file=output)
                        else:
                            print(previous, end = "", file=output)
                        inside_bio = "true"
                    else:
                        print(previous, end = "", file=output)
            else:
                print(previous, end = "", file=output)
            previous = line
        print(previous, end = "", file=output)

    elif (sys.argv[2] == "minusI"):
        inside_bio = "false"
        for line in file:
            if (not line.isspace()):
                split_line = line.split()
                if (split_line[1][0] == "B"):
                    inside_bio = "true"
                    print(line, end = "", file=output)
                if (split_line[1][0] == "O"):
                    inside_bio = "false"
                    print(line, end = "", file=output)
                if (split_line[1][0] == "I"):
                    if (inside_bio == "false"):
                        print(split_line[0] + "\t" + "O", file=output)
                    else:
                        print(line, end = "", file=output)
            else:
                print(line, end = "", file=output)
        
    file.close()
    output.close()

#python3 bio-fixer.py [name_of_file] [addB or minusI]
#if you want to fix the organization results, make sure to change line 24 with this:
#print(previous_split[0] + "\t" + "B-ORGANIZATION", file=output)
