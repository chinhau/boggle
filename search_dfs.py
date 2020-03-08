def recursion(board, i, j, n, visited_set, trie, possible_word, output_set):
    '''Use recursion to find possible words'''

    # Base Case
    if i < 0 or i >= n or j < 0 or j >= n or (i, j) in visited_set:
        return

    char = board[i][j]

    if trie.next[char]:
        possible_word += char
        visited_set.add((i, j))
        if trie.next[char].end:
            output_set.add(possible_word)

        neighbor_list = []
        for a in range(-1, 2):
            for b in range(-1, 2):
                neighbor_list.append((i+a, j+b))

        for a, b in neighbor_list:
            recursion(board, a, b, n, visited_set, trie.next[char],
                      possible_word, output_set)


def dfs(num, board, trie):
    '''Use dfs to find possible words'''
    output = set()
    for i in range(num):
        for j in range(num):
            t = trie.root
            visited = set()
            recursion(board, i, j, num, visited, t, "", output)

    return output
