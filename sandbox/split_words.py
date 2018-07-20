
# A - Z 65 - 90
# a - z 97 - 122

# HelloWorld
def split_words(string):
    words = []
    current_word = [string[0]]
    i = 1
    while i < len(string):
        char = string[i]
        if 'A' <= char <= 'Z':
            words.append(''.join(current_word))
            current_word = [char]
        elif 'a' <= char <= 'z':
            current_word.append(char)
        i += 1

    words.append(''.join(current_word))
    return words

if __name__ == '__main__':
    print(split_words("HelloWorld"))