
def main():
    book_path = "books/frankenstein.txt"
    text = get_words(book_path)
    lower_text = convert_to_lower(text)
    letter_count = count_letters(lower_text)
    count = count_words(text)
    sorted_list = sort_dictionary(letter_count)
        
    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document")
    print("")
    for letter, number in sorted_list:
        if letter.isalpha():
            print(f"The '{letter}' character was found {number} times")
    print("--- End report ---")

#Reads file to a string "text"
def get_words(path):
    with open(path) as f:
        return f.read()

#Converts string to lowercase
def convert_to_lower(text):
    return text.lower()

#Counts the number of words in the string "text" and returns as "count"
def count_words(text):
    words = text.split()
    return len(words)    

def count_letters(lower_text):
    letters = {}
    for l in lower_text:
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1
    return letters

def sort_dictionary(letter_count):
    return sorted(letter_count.items(),reverse=True, key=lambda x: x[1])

main()
