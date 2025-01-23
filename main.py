import itertools
import string
import sys

space = string.digits + string.ascii_lowercase

def generate(length):
    for combination in itertools.product(space, repeat=length):
        yield ''.join(combination)

def main():
    file = open("wordlist.txt", "w")
    for length in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
        for word in generate(length):
            file.write(word + "\n")
    file.close()

if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print("Usage: main.py minLength maxLength")
        sys.exit()
    main()
