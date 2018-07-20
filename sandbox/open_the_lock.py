import collections

def open_lock(deadends, target):
    """
    :type deadends: List[str]
    :type target: str
    :rtype: int
    """
    deadset = set(deadends)
    queue = collections.deque([('0000', 0)])
    seen = {'0000'}
    while queue:
        node, depth = queue.popleft()
        if node == target:
            return depth
        if node in deadset:
            continue
        for neighbor in neighbors(node):
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append((neighbor, depth + 1))
    return -1


# def neighbors(node):
#     s1, s2, s3, s4 = node
#     neighbors = []
#     neighbors.append(str((int(s1) + 1)%10) + s2 + s3 + s4)
#     neighbors.append(str((int(s1) - 1)%10) + s2 + s3 + s4)
#     neighbors.append(s1 + str((int(s2) + 1)%10) + s3 + s4)
#     neighbors.append(s1 + str((int(s2) - 1)%10) + s3 + s4)
#     neighbors.append(s1 + s2 + str((int(s3) + 1)%10) + s4)
#     neighbors.append(s1 + s2 + str((int(s3) - 1)%10) + s4)
#     neighbors.append(s1 + s2 + s3 + str((int(s4) + 1)%10))
#     neighbors.append(s1 + s2 + s3 + str((int(s4) - 1)%10))
#     return neighbors

def neighbors(node):
    for i in range(4):
        int_val = int(node[i])
        for diff in (-1, 1):
            yield node[:i] + str((int_val+diff)%10) + node[i+1:]


if __name__ == '__main__':
    deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
    target = "8888"
    print(open_lock(deadends, target))
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"
    print(open_lock(deadends, target))

