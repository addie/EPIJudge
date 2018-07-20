def generateAbbreviations(word):
    def helper(word, pos, cur, count, result):
        if len(word) == pos:
            # Once we reach the end, append current to the result
            if count > 0:
                cur += str(count)
            result.append(cur)
        else:
            # Skip current position, and increment count
            helper(word, pos + 1, cur, count + 1, result)
            # Include current position, and zero-out count
            if count > 0:
                cur += str(count)
            helper(word, pos + 1, cur + word[pos], 0, result)

    result = []
    helper(word, 0, '', 0, result)
    return result


if __name__ == '__main__':
    print(generateAbbreviations("word"))