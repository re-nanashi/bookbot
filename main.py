def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    # Get number of words
    num_words = get_num_words(text)
    # Create a char count dictionary
    chars_dict = get_char_dict(text)
    # Store the char count info into list then sort into descending order
    chars_list = store_cdict_to_sorted_list(chars_dict)

    # Output to console
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for char_info in chars_list:
        print(
            f"The '{char_info['char']}' character was found {char_info['count']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


# Convert dictionary of characters into a list of dictionaries
def get_char_dict(text):
    # Count the frequency of characters
    chars = {}
    for char in text:
        lowered = char.lower()
        # Skip loop if char is not alphabet
        if not lowered.isalpha():
            continue
        # Store the charactes into the chars dictionary
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


# Store all character info into a list
def store_cdict_to_sorted_list(dict):
    sorted_list = []
    for char in dict:
        sorted_list.append({"char": char, "count": dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def sort_on(dict):
    return dict["count"]


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
