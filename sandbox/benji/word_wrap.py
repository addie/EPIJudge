def word_wrap(words, width):
    words = words.split()
    curr = 0
    for i, word in enumerate(words):
        len_word = len(word)
        if len_word > width:
            raise IndexError('Word is longer than line')
        if curr + len_word < width:
            curr += len_word+1
            if curr < width:
                words[i] += ' '
        elif curr + len_word == width:
            curr += len_word
        else:
            words[i] = '\n' + words[i] + ' '
            curr = len(words[i])+1
    return ''.join(words)


INF = float('inf')
def word_wrap_dp(words, width):
    words = words.split()
    cost = [[0 for _ in range(len(words))] for _ in range(len(words))]
    for i in range(len(words)):
        cost[i][i] = width - len(words[i])
        for j in range(i+1, len(words)):
            cost[i][j] = cost[i][j-1]-len(words[j])-1
    for i in range(len(words)):
        for j in range(i, len(words)):
            cost[i][j] = INF if cost[i][j] < 0 else cost[i][j]**2
    min_cost, result = [0] * len(words), [0] * len(words)
    for i in range(len(words)-1, -1, -1):
        min_cost[i] = cost[i][len(words)-1]
        result[i] = len(words)
        for j in range(len(words)-1, i, -1):
            if cost[i][j-1] == INF:
                continue
            if min_cost[i] > min_cost[j] + cost[i][j - 1]:
                min_cost[i] = min_cost[j] + cost[i][j-1]
                result[i] = j

    output = build_output(words, min_cost, result)
    return ''.join(output)

def build_output(words, min_cost, result):
    i = 0
    print("Minimum cost is {}".format(min_cost[0]))
    builder = []
    j = result[i]
    for k in range(i, j):
        builder.append(words[k])
        builder.append(" ")
    builder.append("\n")
    i = j
    while j < len(words):
        j = result[i]
        for k in range(i, j):
            builder.append(words[k])
            builder.append(" ")
        builder.append("\n")
        i = j
    return builder

if __name__ == '__main__':
    line = 25
    sentence = "This is a problem presented by geeks for geeks on the website word wrap problem"
    wrapped = word_wrap(sentence, line)
    print(wrapped)
    assert wrapped == 'This is a problem \npresented by geeks for\ngeeks on the website \nword wrap problem '

    print()

    line = 25
    sentence = "This is a problem presented by geeks for geeks on the website word wrap problem"
    wrapped = word_wrap_dp(sentence, line)
    print(wrapped)
    assert wrapped == 'This is a problem \npresented by geeks for \ngeeks on the website \nword wrap problem \n'
