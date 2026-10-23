
def get_book_text(file: str) -> str:
    with open(file) as f:
        file_contents = f.read()

    return file_contents

def get_num_words(text: str) -> int:
    return len(text.split())

def get_letter_count(word_list) -> dict:

    #Initialize dictionary of lower case letters
    letters = {chr(i+96):0 for i in range(1,27)}

    for word in word_list:
        for letter in word:
            if (letter.lower() in letters):
                temp = letter.lower()
                letters[temp] += 1
            else:
                temp = letter.lower()
                letters[temp] = 1
    return letters

def sort_on(character: tuple[str, int]) -> int:
    return character[1]

def chars_dict_to_sorted_list(counts: dict[str, int]) -> list[tuple[str, int]]:
    out = []
    for key in counts.keys():
        out.append((key, counts[key]))

    sorted_out = sorted(out, reverse=True, key=sort_on)

    return sorted_out
