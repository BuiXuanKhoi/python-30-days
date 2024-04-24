import json

def count_lines_and_words(file_path):
    words = 0
    lines = 0
    with open(file_path) as file:
        content = file.readlines()
        for line in content:
            words += len(line.split())
            lines += 1
    
    return (lines, words)


def find_top_most_spoken_languages(file_path, number):
    with open(file_path, 'r', encoding='utf-8') as file :
        d = json.load(file)
    print(d)


print(count_lines_and_words('./file-handling/data/obama_speech.txt'))
print(count_lines_and_words('./file-handling/data/michelle_obama_speech.txt'))

print(find_top_most_spoken_languages('./file-handling/data/countries_data.json', 3))

