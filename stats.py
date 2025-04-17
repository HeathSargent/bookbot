def count_words(str):
    split_string = str.split()
    return len(split_string)

def count_characters(str):
    character_count = {}
    for character in str:
        lower_char = character.lower()
        if lower_char in character_count:
            character_count[lower_char] += 1
        else:
            character_count[lower_char] = 1
    return character_count

def sort_on(dict):
    return dict["num"]

def sort_character_count(character_counts):
    dict_array = []
    for key in character_counts:
        dict_array.append({"name":key,"num":character_counts[key]})

    dict_array.sort(reverse=True, key=sort_on)
    return dict_array