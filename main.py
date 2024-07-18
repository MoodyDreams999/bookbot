def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        y = file_contents.lower()
        x = len(file_contents.split())
        print("word count:", x)
        char_countTrns = stringDet(y)
        sort_dict_by_value(char_countTrns)
        #print("Character count:", sorted_char_count)
        return (y),(char_countTrns)
        
# returns the number of times each character appears in a string, converting to lowercase to ensure no duplicates.
def stringDet(y):
    char_count = {}
    for char in y:
        if char.isalpha():
            if char in char_count:
                char_count[char] +=1
            else:
                char_count[char] = 1
    return char_count
            
def sort_dict_by_value(d):
    sorted_dict = sorted(d.items(), key=lambda item: item[1], reverse=True)
    for d, key in sorted_dict:
        bestFormat = print(f"The {d} character was found {key} times.")
    return bestFormat

if __name__ == "__main__":
    main()