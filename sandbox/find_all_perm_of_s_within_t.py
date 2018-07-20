from collections import Counter
def find_perm_of_p_within_s(p, s):
    p_count = Counter(p)
    s_count = Counter(s[:len(p)-1])
    # Don't need to init full alphabet if delete removed chars from map
    # for letter in range(ord('a'), ord('z')+1):
    #     p_count[chr(letter)] = 0 if not p_count[chr(letter)] else p_count[chr(letter)]
    #     s_count[chr(letter)] = 0 if not s_count[chr(letter)] else s_count[chr(letter)]
    perms = []
    for i in range(len(p)-1, len(s)):
        s_count[s[i]] += 1
        if s_count == p_count:
            perms.append(i-len(p)+1)
        s_count[s[i-len(p)+1]] -= 1
        if s_count[s[i-len(p)+1]] == 0:
            del s_count[s[i-len(p)+1]]
    return perms


if __name__ == '__main__':
    p = "xacxzaa"
    s = "fxaazxacaaxzoecazxaxaz"
    perms = find_perm_of_p_within_s(p, s)
    print(perms)