FRANKENSTEIN_PATH = "books/frankenstein.txt"

def string_to_char_count(string: str) -> dict[str, int]:
    char_to_count = {}
    string = string.lower()
    chars = []
    for _, val in enumerate(string):
        if val.isalpha():
            chars.append(val)

    for char in chars:
        if char not in char_to_count:
            char_to_count[char] = 1
        else:
            char_to_count[char] += 1

    return char_to_count

def update_dict_vals(
        current_char_to_count: dict[str, int],
        new_char_to_count: dict[str, int]
    ) -> dict[str, int]:
    updated_char_to_count = current_char_to_count

    for key, val in new_char_to_count.items():
        if key in current_char_to_count.keys():
            updated_char_to_count[key] += val
        else:
            updated_char_to_count[key] = val

    return updated_char_to_count

def text_to_char_count(text: list[str]) -> dict[str, int]:
    char_to_count = {}
    for word in text:
        update_dict_vals(char_to_count, string_to_char_count(word))

    return char_to_count

def print_text_file_report(text_file_path: str) -> None:
    header_str = f"--- Begin report of {text_file_path} ---"
    tail_str = "--- End report ---"

    words = []
    with open(text_file_path) as file:
        contents = file.read()
        words = contents.split()

    char_to_count = text_to_char_count(words)
    char_to_count = {
        k: v for k, v in sorted(
            char_to_count.items(),
            key=lambda item: item[1],
            reverse=True
        )
    }

    print(header_str)
    print(f"{len(words)} words found in the document\n")
    for key, val in char_to_count.items():
        print(f"The '{key}' character was found {val} times")
    print(tail_str)

if __name__ == "__main__":
    print_text_file_report(FRANKENSTEIN_PATH)

