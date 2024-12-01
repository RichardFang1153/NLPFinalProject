import sys
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag


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
        count = 0
        for line in file:
            count = 0
            if (not line.isspace()):
                sentence = line.split()
                inside_label_type = "false"
                current_type = ""
                inside_label = "false"
                begin = "false"
                no_label_sentence = ""
                for index in range(1, len(sentence)):
                    if (("<" not in sentence[index]) and (">" not in sentence[index])):
                        no_label_sentence = no_label_sentence + " " + sentence[index]
                tokenized = word_tokenize(no_label_sentence)
                tagged_sentence = nltk.pos_tag(tokenized)        
                for word in sentence:
                    if (word != sentence[0]):
                        if ((word[0] == "<") and (word[1] != "/")):
                            inside_label_type = "true"
                        elif (inside_label_type == "true"):
                            current_type = word[0:-1]
                            inside_label_type = "false"
                            inside_label = "true"
                            begin = "true"
                        elif (inside_label == "true"):
                            if (begin == "true"):
                                if (word_group in current_type):
                                    print(word + "\t" + tagged_sentence[count][1] + "\t" + "B-" + word_group, file=t_output)
                                    count = count + 1
                                else:
                                    print(word + "\t" + tagged_sentence[count][1] + "\t" + "O", file=t_output)
                                    count = count + 1
                                begin = "false"
                            elif (word[0:2]!= "</"):
                                if (word_group in current_type):
                                    print(word + "\t" + tagged_sentence[count][1] + "\t" + "I-" + word_group, file=t_output)
                                    count = count + 1
                                else:
                                    print(word + "\t" + tagged_sentence[count][1] + "\t" + "O", file=t_output)
                                    count = count + 1
                            elif (word[0:2]== "</"):
                                inside_label = "false"
                                current_type = ""
                        else:
                            print(word + "\t" + tagged_sentence[count][1] + "\t" + "O", file=t_output)
                            count = count + 1
                print("", file=t_output) 
        t_output.close()

        
    elif (sys.argv[2] == "other"):
        answer_key = open("dev_or_test.POS-chunk", "w")
        o_output = open("dev_or_test.POS", "w")
        count = 0
        for line in file:
            count = 0
            if (not line.isspace()):
                sentence = line.split()
                inside_label_type = "false"
                current_type = ""
                inside_label = "false"
                begin = "false"
                no_label_sentence = ""
                for index in range(1, len(sentence)):
                    if (("<" not in sentence[index]) and (">" not in sentence[index])):
                        no_label_sentence = no_label_sentence + " " + sentence[index]
                tokenized = word_tokenize(no_label_sentence)
                tagged_sentence = nltk.pos_tag(tokenized)        
                for word in sentence:
                    if (word != sentence[0]):
                        if ((word[0] == "<") and (word[1] != "/")):
                            inside_label_type = "true"
                        elif (inside_label_type == "true"):
                            current_type = word[0:-1]
                            inside_label_type = "false"
                            inside_label = "true"
                            begin = "true"
                        elif (inside_label == "true"):
                            if (begin == "true"):
                                if (word_group in current_type):
                                    print(word + "\t" + tagged_sentence[count][1] + "\t" + "B-" + word_group, file=answer_key)
                                    print(word + "\t" + tagged_sentence[count][1], file=o_output)
                                    count = count + 1
                                else:
                                    print(word + "\t" + tagged_sentence[count][1] + "\t" + "O", file=answer_key)
                                    print(word + "\t" + tagged_sentence[count][1], file=o_output)
                                    count = count + 1
                                begin = "false"
                            elif (word[0:2]!= "</"):
                                if (word_group in current_type):
                                    print(word + "\t" + tagged_sentence[count][1] + "\t" + "I-" + word_group, file=answer_key)
                                    print(word + "\t" + tagged_sentence[count][1], file=o_output)
                                    count = count + 1
                                else:
                                    print(word + "\t" + tagged_sentence[count][1] + "\t" + "O", file=answer_key)
                                    print(word + "\t" + tagged_sentence[count][1], file=o_output)
                                    count = count + 1
                            elif (word[0:2]== "</"):
                                inside_label = "false"
                                current_type = ""
                        else:
                            print(word + "\t" + tagged_sentence[count][1] + "\t" + "O", file=answer_key)
                            print(word + "\t" + tagged_sentence[count][1], file=o_output)
                            count = count + 1
                print("", file=answer_key)
                print("", file=o_output)
        answer_key.close()
        o_output.close()

    file.close()
