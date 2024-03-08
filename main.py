final_diction = {}

def main():
    book_path = "books/frankenstein.txt"
    book_text = console_book_printer(book_path)
    word_count = counting_words_as_stars(book_text)
    letter_counted = letter_counter(book_text)
    #print(book_text)
    print('--- Begin report of books/frankenstein.txt ---')
    print(f"{word_count} words found in the document\n")
    print(letter_counted)
    print('--- End report ---')

def console_book_printer(path):
    with open(path) as f:
        return f.read()

def counting_words_as_stars(words):
    counter = words.split()
    return len(counter)

def letter_counter(text):  
    lowered_text = text.lower()
    split_letters = list(lowered_text)
    initial_letter = ""
    report_char = ""
    for letter in split_letters:      
        if letter not in final_diction and letter.isalpha():
            count = 0
            initial_letter = letter
            for i in range(0, len(split_letters)):     
                if split_letters[i] == initial_letter:
                    count += 1
            final_diction[letter] = count
            report_char = report_char + 'The \'' + letter + '\' was found ' + str(count) + ' times\n'
    #return final_diction
    return report_char

main()