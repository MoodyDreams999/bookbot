def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        x = len(file_contents.split())
        print(x)


if __name__ == "__main__":
    main()