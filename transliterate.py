import re
import sys

def main():
    pairs = []
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip()
            pair = line.split(': ')
            pairs.append(pair)
            
    for line in sys.stdin:
        line.rstrip()
        print(transLit(line, pairs))

def transLit(text, pairs):
    out = text.lower()
    for pair in pairs:
        out= re.sub(pair[0], pair[1], out)
    return out
if __name__ == "__main__":
    main()