import sys
import os
from collections import defaultdict

def score(keyFileName, responseFileName):
    keyFile = open(keyFileName, 'r')
    key = keyFile.readlines()
    responseFile = open(responseFileName, 'r')
    response = responseFile.readlines()

    if len(key) != len(response):
        print("Length mismatch between key and response file")
        return

    # Variables for tagging scores
    correct = 0
    incorrect = 0
    keyGroupCount = 0
    responseGroupCount = 0
    correctGroupCount = 0

    # Variables for B-cubed scoring
    key_clusters = defaultdict(set)
    response_clusters = defaultdict(set)

    key_start = None
    response_start = None

    for i in range(len(key)):
        key[i] = key[i].strip()
        response[i] = response[i].strip()

        if key[i] == "":
            if response[i] != "":
                print(f"Sentence mismatch at line {i}")
                return
            continue

        key_fields = key[i].split('\t')
        response_fields = response[i].split('\t')

        if len(key_fields) != 2 or len(response_fields) != 2:
            print(f"Format error at line {i}")
            print(f"Key line: '{key[i]}' (Fields: {len(key_fields)})")
            print(f"Response line: '{response[i]}' (Fields: {len(response_fields)})")
            return

        key_token, key_tag = key_fields
        response_token, response_tag = response_fields

        if key_token != response_token:
            print(f"Token mismatch at line {i}")
            return

        # Tagging correctness
        if key_tag == response_tag:
            correct += 1
        else:
            incorrect += 1
            print("Line: " + str(i) + "    Answer Key: " + key_token + " = " + key_tag + "   Our output: " + response_token + " = " + response_tag)

        # Group count for tagging
        key_label = key_tag.split('-')[0]  # Correcting to split by '-' instead of space
        response_label = response_tag.split('-')[0]

        if key_label == 'B':
            keyGroupCount += 1
        if response_label == 'B':
            responseGroupCount += 1
        if key_tag == response_tag and key_label == 'B':
            correctGroupCount += 1

        # Clustering for B-cubed
        if key_tag != "O":
            key_clusters[key_token].add(key_tag.split('-')[1])
        if response_tag != "O":
            response_clusters[response_token].add(response_tag.split('-')[1])

    # Accuracy, Precision, Recall, F1 for tagging
    print(f"{correct} out of {correct + incorrect} tags correct")
    accuracy = 100.0 * correct / (correct + incorrect)
    precision = 100.0 * correctGroupCount / responseGroupCount if responseGroupCount > 0 else 0.0
    recall = 100.0 * correctGroupCount / keyGroupCount if keyGroupCount > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0

    print("Tagging Scores:")
    print(f"  Accuracy: {accuracy:.2f}%")
    print(f"  Precision: {precision:.2f}%")
    print(f"  Recall: {recall:.2f}%")
    print(f"  F1 Score: {f1:.2f}%")

def main(args):
    if len(args) != 3:
        print("Usage: python3 score.chunk.py <key_file> <response_file>")
        return
    key_file = args[1]
    response_file = args[2]
    score(key_file, response_file)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
