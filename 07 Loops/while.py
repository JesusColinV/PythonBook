# This is an exercise file from Python 3 Training by Jesus Colín

def main():
    # simple fibonacci series
    # the sum of two elements defines the next set
    a, b = 0, 1
    while b < 50:
        print(b, end=' ')
        a, b = b, a + b

if __name__ == "__main__": main()
