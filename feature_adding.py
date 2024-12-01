import sys

def extract_training_features(training_file, output_file):
    with open(training_file, 'r') as f:
        lines = f.read().strip().split("\n")

    with open(output_file, "w") as output:
        for i in range(len(lines)):
            if lines[i] == "":
                print("", file=output)
                continue

            current_line = lines[i].split()

            if len(current_line) < 3:
                continue

            token, pos, chunk_tag = current_line[0], current_line[1], current_line[2]

            print(f"{token}\tPOS={pos}", end="", file=output)


            if i > 1 and lines[i-2] != "":
                two_prev = lines[i-2].split()
                print(f"\t2_prev_word={two_prev[0]}\t2_prev_POS={two_prev[1]}", end="", file=output)

            if i > 0 and lines[i-1] != "":
                prev = lines[i-1].split()
                print(f"\tprev_word={prev[0]}\tprev_POS={prev[1]}", end="", file=output)

            if i < len(lines) - 1 and lines[i+1] != "":
                next = lines[i+1].split()
                print(f"\tnext_word={next[0]}\tnext_POS={next[1]}", end="", file=output)

            if i < len(lines) - 2 and lines[i+2] != "":
                two_next = lines[i+2].split()
                print(f"\t2_next_word={two_next[0]}\t2_next_POS={two_next[1]}", end="", file=output)


            print(f"\t{chunk_tag}", file=output)

def extract_test_features(test_file, output_file):
    with open(test_file, 'r') as f:
        lines = f.read().strip().split("\n")

    with open(output_file, "w") as output:
        for i in range(len(lines)):
            if lines[i] == "":
                print("", file=output)
                continue

            current_line = lines[i].split()

            if len(current_line) < 2:
                continue

            token, pos = current_line[0], current_line[1]

            print(f"{token}\tPOS={pos}", end="", file=output)

            if i > 1 and lines[i-2] != "":
                two_prev = lines[i-2].split()
                print(f"\t2_prev_word={two_prev[0]}\t2_prev_POS={two_prev[1]}", end="", file=output)

            if i > 0 and lines[i-1] != "":
                prev = lines[i-1].split()
                print(f"\tprev_word={prev[0]}\tprev_POS={prev[1]}", end="", file=output)

            if i < len(lines) - 1 and lines[i+1] != "":
                next = lines[i+1].split()
                print(f"\tnext_word={next[0]}\tnext_POS={next[1]}", end="", file=output)

            if i < len(lines) - 2 and lines[i+2] != "":
                two_next = lines[i+2].split()
                print(f"\t2_next_word={two_next[0]}\t2_next_POS={two_next[1]}", end="", file=output)


            print("", file=output)

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 feature_extraction.py <training_file> <test_file>")
        return

    training_file, test_file = sys.argv[1], sys.argv[2]

    extract_training_features(training_file, "training.feature")
    extract_test_features(test_file, "test.feature")

if __name__ == "__main__":
    main()
