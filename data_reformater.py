import sys



if (len(sys.argv) != 4):
    print("Not enough arguments")
else:
    word_group = sys.argv[3]
    original_file = open(sys.argv[1], "r")
    temp_output = open("temp.txt", "w")
    for line in original_file:
        for char in line:
            if (char == "<"):
                print(" ", end = "", file=temp_output)
                print(char , end = "", file=temp_output)
            elif (char == ">"):
                print(char , end = "", file=temp_output)
                print(" ", end = "", file=temp_output)
            else:
                print(char , end = "", file=temp_output)
    temp_output.close()
    file = open("temp.txt", "r")
    if (sys.argv[2] == "training"):
        
        t_output = open("training.POS-chunk", "w")
        
        for line in file:
            if (not line.isspace()):
                sentence = line.split()
                print(sentence , file=t_output)
                inside_label_type = "false"
                current_type = ""
                inside_label = "false"
                begin = "false"
                for word in sentence:
                    if (word != sentence[0]):
                        if ((word[0] == "<") and (word[1] != "/")):
                            inside_label_type = "true"
                        elif (inside_label_type == "true"):
                            current_type = word[0:-1]
                            inside_label_type = "false"
                            inside_label = "true"
                            begin = "true"
                        elif ((word[0] != "<") and (inside_label == "true")):
                            if (begin == "true"):
                                print(word + "\t" + "B-" + current_type, file=t_output)
                                begin = "false"
                            elif (word[0:2]!= "</"):
                                print(word + "\t" + "I-" + current_type, file=t_output)
                            elif (word[0:2]== "</"):
                                inside_label = "false"
                                current_type = ""
                                
                                
                                                
                        
                
        t_output.close()
        
    elif (sys.argv[2] == others):
        print("Not yet implemented")

    file.close()
        

        
#python3 data_reformater.py training_data_combined.txt training date
