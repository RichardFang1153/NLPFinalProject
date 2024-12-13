import sys
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

if len(sys.argv) != 4:
    print("Not enough arguments")
else:
    word_group = sys.argv[3]
    original_file = open(sys.argv[1], "r")
    temp_output = open("temp.txt", "w")
    for line in original_file:
        for char in line:
            if char == "<":
                print(" ", end="", file=temp_output)
                print(char, end="", file=temp_output)
            elif char == ">":
                print(char, end="", file=temp_output)
                print(" ", end="", file=temp_output)
            else:
                print(char, end="", file=temp_output)
    temp_output.close()
    file = open("temp.txt", "r")

    if sys.argv[2] == "training":
        t_output = open("training.POS-chunk", "w")
        count = 0
        for line in file:
            count = 0
            if not line.isspace():
                sentence = line.split()
                inside_label_type = "false"
                current_type = ""
                inside_label = "false"
                begin = "false"
                no_label_sentence = ""
                labels = []
                for index in range(1, len(sentence)):
                    if "<" not in sentence[index] and ">" not in sentence[index]:
                        no_label_sentence += " " + sentence[index]

                tokenized = word_tokenize(no_label_sentence)
                tagged_sentence = nltk.pos_tag(tokenized)
                for word in sentence:
                    if word != sentence[0]:
                        if word.startswith("<") and not word.startswith("</"):
                            inside_label_type = "true"
                        elif inside_label_type == "true":
                            current_type = word[:-1]
                            inside_label_type = "false"
                            inside_label = "true"
                            begin = "true"
                        elif inside_label == "true":
                            if begin == "true":
                                labels.append("B-" + word_group if word_group in current_type else "O")
                                begin = "false"
                            elif not word.startswith("</"):
                                labels.append("I-" + word_group if word_group in current_type else "O")
                            elif word.startswith("</"):
                                labels[-1] = labels[-1].replace("I-", "L-")
                                inside_label = "false"
                                current_type = ""
                        else:
                            labels.append("O")

                #Convert isolated Bs into Us
                for i in range(len(labels)):
                    if labels[i].startswith("B-") and (i + 1 >= len(labels) or not labels[i + 1].startswith("I-")):
                        labels[i] = labels[i].replace("B-", "U-")

                for idx, word in enumerate(tokenized):
                    print(word + "\t" + tagged_sentence[idx][1] + "\t" + labels[idx], file=t_output)

                print("", file=t_output)
        t_output.close()

    elif sys.argv[2] == "other":
        answer_key = open("dev_or_test.chunk", "w")
        o_output = open("dev_or_test.POS", "w")
        count = 0
        for line in file:
            count = 0
            if not line.isspace():
                sentence = line.split()
                inside_label_type = "false"
                current_type = ""
                inside_label = "false"
                begin = "false"
                no_label_sentence = ""
                labels = []

                for index in range(1, len(sentence)):
                    if "<" not in sentence[index] and ">" not in sentence[index]:
                        no_label_sentence += " " + sentence[index]

                tokenized = word_tokenize(no_label_sentence)
                tagged_sentence = nltk.pos_tag(tokenized)

                for word in sentence:
                    if word != sentence[0]:
                        if word.startswith("<") and not word.startswith("</"):
                            inside_label_type = "true"
                        elif inside_label_type == "true":
                            current_type = word[:-1]
                            inside_label_type = "false"
                            inside_label = "true"
                            begin = "true"
                        elif inside_label == "true":
                            if begin == "true":
                                labels.append("B-" + word_group if word_group in current_type else "O")
                                begin = "false"
                            elif not word.startswith("</"):
                                labels.append("I-" + word_group if word_group in current_type else "O")
                            elif word.startswith("</"):
                                labels[-1] = labels[-1].replace("I-", "L-")
                                inside_label = "false"
                                current_type = ""
                        else:
                            labels.append("O")

                #Convert isolated Bs into Us
                for i in range(len(labels)):
                    if labels[i].startswith("B-") and (i + 1 >= len(labels) or not labels[i + 1].startswith("I-")):
                        labels[i] = labels[i].replace("B-", "U-")

                for idx, word in enumerate(tokenized):
                    print(word + "\t" + labels[idx], file=answer_key)
                    print(word + "\t" + tagged_sentence[idx][1], file=o_output)
                print("", file=answer_key)
                print("", file=o_output)
        answer_key.close()
        o_output.close()

    file.close()
