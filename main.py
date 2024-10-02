def main():
    with open("books/frankenstein.txt") as f:
        print(f)
        file_contents = f.read()
        w_count = count_words(file_contents)
        c_count = count_characters(file_contents)
        report(w_count, c_count)
    
def count_words(file_contents):
    count = 0
    words = file_contents.split()
    for word in words:
        count += 1
    return count

def count_characters(file_contents):
    l_file_contents = file_contents.lower()
    count = {}
    for letter in l_file_contents:
        if letter in count:
            count[letter] += 1
        elif letter not in count:
            count[letter] = 1
    return count

def report(w_count, c_count):
    max_so_far = 40000
    f_path = "books/frankenstein.txt"
    print(f"=== Begin report of {f_path} ===")
    print(f"{w_count} words found in the document.")
    for chr in c_count:
        key = c_count[chr]
        if chr.isalpha():
            print(f"The ({chr}) character was found {key} times.")
    print("=== End of report ===")
main()