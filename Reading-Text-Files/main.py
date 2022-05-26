# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open(filename) as file:
        lines = file.read()
        print(lines)
        return lines


def count_words():
    text = read_file_content("./story.txt")
    unique_words = {}
    passage = text.split(' ')
    for word in passage:
        unique_words[word] = unique_words.get(word, 0)+1
    print(unique_words)
