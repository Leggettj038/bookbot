
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
    #Searchs through the "sorted_list" dictionary for a letter and outputs how many times that letter appears
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

#Counts the number of times a letter appears and adds it to the dictionary "letters", returned to "letter_count"
def count_letters(lower_text):
    letters = {}
    for l in lower_text:
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1
    return letters

#Sorts the "letters_count" dictionary based on the number of times a character appears into a new dictionary called "sorted_list" 
def sort_dictionary(letter_count):
    return sorted(letter_count.items(),reverse=True, key=lambda x: x[1])

main()
