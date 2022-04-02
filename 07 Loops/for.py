# This is an exercise file from Python 3 Training by Jesus Colín

def main():
    fh = open('lines.txt')
    for line in fh.readlines():
        print(line)

if __name__ == "__main__": main()
