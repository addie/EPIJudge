def is_matched(expression):
    s = []
    for char in expression:
        if char == '(':
            s.append(')')
        elif char == '[':
            s.append(']')
        elif char == '{':
            s.append('}')
        elif not s or char != s.pop():
            return False
    return True if not s else False

if __name__ == '__main__':
    t = ['{()[][{}]}','({}{[]})({)}','()[]','[()][{}]{[({})[]]}[','((){)}']
    for exp in t:
        if is_matched(exp):
            print("YES")
        else:
            print("NO")

